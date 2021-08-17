import os

from gradgpad.foundations.results.results_provider import ResultsProvider
from gradgpad.foundations.scores.approach import Approach
from gradgpad.foundations.scores.protocol import Protocol
from gradgpad.tools.visualization.gif_creator import GifCreator
from gradgpad.tools.visualization.radar.combined_scenario import CombinedScenario
from gradgpad.tools.visualization.radar.create_apcer_detail import WorkingPoint
from gradgpad.tools.visualization.radar.pad_radar_pai_plotter import PadRadarPaiPlotter


def calculate_pad_radar_by_pai(output_path: str):
    print("> Novel Visualizations | Calculating PAD-radar (APCER by PAI)...")

    output_path_apcer_by_pais = f"{output_path}/radar/apcer_by_pais"
    os.makedirs(output_path_apcer_by_pais, exist_ok=True)

    results = {
        "Quality": ResultsProvider.get(
            Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
        ),
        "Auxiliary": ResultsProvider.get(
            Approach.AUXILIARY, protocol=Protocol.GRANDTEST
        ),
    }

    selected_working_points = {
        "APCER @ BPCER 1 %": WorkingPoint.BPCER_1,
        "APCER @ BPCER 5 %": WorkingPoint.BPCER_5,
        "APCER @ BPCER 10 %": WorkingPoint.BPCER_10,
        "APCER @ BPCER 15 %": WorkingPoint.BPCER_15,
        "APCER @ BPCER 20 %": WorkingPoint.BPCER_20,
        "APCER @ BPCER 25 %": WorkingPoint.BPCER_25,
        "APCER @ BPCER 30 %": WorkingPoint.BPCER_30,
        "APCER @ BPCER 35 %": WorkingPoint.BPCER_35,
        "APCER @ BPCER 40 %": WorkingPoint.BPCER_40,
        "APCER @ BPCER 45 %": WorkingPoint.BPCER_45,
        "APCER @ BPCER 50 %": WorkingPoint.BPCER_50,
    }

    filenames_pais_types = {}

    for title, working_point in selected_working_points.items():
        combined_scenarios = {"test_type_I_and_II": CombinedScenario.PAS_I_AND_II}

        for pais_type, combined_scenario in combined_scenarios.items():
            for extension in ["pdf", "png"]:
                output_filename = f"{output_path_apcer_by_pais}/grandtest_trained_type_pai_I_{pais_type}_{working_point.value}_radar_chart.{extension}"

                if pais_type not in filenames_pais_types:
                    filenames_pais_types[pais_type] = [output_filename]
                else:
                    filenames_pais_types[pais_type].append(output_filename)

                plotter = PadRadarPaiPlotter(
                    title=title,
                    working_point=working_point,
                    combined_scenario=combined_scenario,
                    fontsize_vertices=15,
                    format=extension if extension == "pdf" else None,
                )
                plotter.save(output_filename, results)

    if filenames_pais_types:
        output_path_apcer_by_pais_gifs = f"{output_path_apcer_by_pais}/gifs/"
        os.makedirs(output_path_apcer_by_pais_gifs, exist_ok=True)

        for pais_type, input_filenames in filenames_pais_types.items():
            output_filename = f"{output_path_apcer_by_pais_gifs}/grandtest_trained_type_pai_I_{pais_type}.gif"
            GifCreator.execute(output_filename, input_filenames)
