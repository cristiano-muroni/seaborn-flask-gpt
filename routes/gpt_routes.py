from flask import Blueprint, request, jsonify, url_for, current_app
from controllers.gpt_controllers import get_completion
from dashboards.dashboard import show_graphs_lm, show_graphs_full, show_graphs_lm_scatter, show_graphs_lm_line
from dashboards.dashboard import show_graphs_full_scatter, show_graphs_full_line, show_graphs_lm_dataframe
from utils.matched_the_word import matched_the_word_graph
from utils.manage_static import manage_static_folder
import os

gpt_routes_bp = Blueprint('gpt_routes', __name__)
deploy_routes_bp = Blueprint('deploy_routes', __name__)

@deploy_routes_bp.route('/', methods=['GET'])
def deploy():
    print("ok deu certo!")
    return "Ok deu certo!"

@gpt_routes_bp.route('/chatbot', methods=['POST'])
def chatbot():
    userInput = request.json.get('content') 
    graph = matched_the_word_graph(userInput)
    print(graph)

    static_folder = current_app.static_folder
    manage_static_folder(static_folder)

    if graph.get('graph') == True :
        if graph.get('last_months') == True :
            if graph.get('scatter_plot') == True:
                graph_path = show_graphs_lm_scatter()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})
            
            elif graph.get('list_chart') == True :
                graph_path = show_graphs_lm_line()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})
            elif graph.get('table') == True :
                graph_path = show_graphs_lm_dataframe()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})
            
            else :
                graph_path = show_graphs_lm()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})
        
        elif graph.get('full_year') == True :
            if graph.get('scatter_plot') == True:
                graph_path = show_graphs_full_scatter()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})
            
            elif graph.get('list_chart') == True :
                graph_path = show_graphs_full_line()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})
            else :
                graph_path = show_graphs_full()
                graph_url = url_for('static', filename=os.path.basename(graph_path))
                return jsonify({"graph_url": graph_url})           
      

    prompt = f"""Você é um chatbot amigável de atendimento da Citrosuco e conforme os dados contidos nesse site abaixo:
    Site: https://www.citrosuco.com.br/governanca/

    COM BASE NA SUA ANALISE DO TEXTO EXTRAIDO DO SITE
    Responda a pergunta do usuário:
    {userInput}
    """ 
    response = get_completion(prompt)    
    return response