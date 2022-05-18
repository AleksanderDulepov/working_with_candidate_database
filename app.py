from flask import Flask, render_template
import utils


def main():
    app = Flask(__name__)

    @app.route('/')
    def general_page():
        candidates_list = utils.load_data()
        if candidates_list:
            return render_template('list.html', candidates=candidates_list)
        return "Список кандидатов пуст"

    @app.route('/candidate/<int:cand_id>')
    def page_by_id(cand_id):
        selected_cand = utils.get_candidate(cand_id)
        if selected_cand is None:
            return "Кандидата с таким id нет в базе"
        return render_template('single.html', name=selected_cand.name,
                               position=selected_cand.position, picture=selected_cand.picture,
                               skills=selected_cand.skills)

    @app.route('/search/<cand_name>')
    def page_by_name(cand_name):
        selected_cand_by_names = utils.get_candidates_by_name(cand_name)
        if selected_cand_by_names:
            return render_template('search.html', amount=len(selected_cand_by_names),
                                   candidates=selected_cand_by_names)
        return "Кандидатов с таким именем нет в базе"

    @app.route('/skill/<cand_skill>')
    def page_by_skill(cand_skill):
        selected_cand_by_skills = utils.get_candidates_by_skill(cand_skill)
        if selected_cand_by_skills:
            return render_template('skill.html', amount=len(selected_cand_by_skills),
                                   skill=cand_skill, candidates=selected_cand_by_skills)
        return "Кандидатов с такими скиллами скиллами нет в базе"

    app.run()


if __name__ == "__main__":
    main()
