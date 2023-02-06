import pytest


@pytest.mark.unit
def test_should_load_annotations():
    from gradgpad import annotations

    assert annotations.num_annotations == 29567


@pytest.mark.unit
def test_should_check_annotations_statistics():
    from gradgpad import annotations

    pai_stats = annotations.statistics()

    assert list(pai_stats.keys()) == [
        "num_genuines",
        "num_attacks",
        "num_samples_pas_type",
        "num_coarse_grained_pai",
        "num_fine_grained_pai",
        "percentage_num_samples_pas_type",
        "percentage_num_coarse_grained_pai",
        "percentage_num_fine_grained_pai",
    ]


@pytest.mark.unit
def test_should_filter_by_ids():
    from gradgpad import annotations

    selected_annotations = annotations.get_annotations_from_ids(
        ["casia-fasd_test_release/1/6.avi"]
    )

    assert len(selected_annotations) == 1


@pytest.mark.unit
def test_should_filter_annotations_by_dataset():
    from gradgpad import annotations

    selected_annotations = annotations.get_annotations_filtered_by_datasets(
        ["replay-mobile"]
    )

    assert len(selected_annotations) == 1030


@pytest.fixture
def expected_pseudo_random_ids_values():
    return [
        "uvad_release_1/attack/sony/sony/monitor4/MAH01472.MP4",
        "oulu-npu_Dev_files/1_1_25_3.avi",
        "siw-m_Mask/TransparentMask/Mask_Trans_58.mov",
        "siw_Test/spoof/082/082-2-3-3-2.mov",
        "oulu-npu_Train_files/4_1_16_5.avi",
        "uvad_release_1/attack/panasonic/nikon/monitor4/DSCN0831.MOV",
        "siw-m_Live/Test/Live_645.mov",
        "siw_Test/spoof/029/029-1-3-1-1.mov",
        "oulu-npu_Dev_files/6_1_35_2.avi",
        "uvad_release_1/attack/olympus/kodac/monitor1/101_0035.MOV",
    ]


#
# @pytest.mark.unit
# def test_should_load_annotations_get_ids_random(expected_pseudo_random_ids_values):
#     from gradgpad import annotations
#
#     assert len(annotations.get_ids(Filter(random_values=10))) == 10
#
#     assert len(annotations.get_ids(Filter(pseudo_random_values=10))) == 10
#
#     assert expected_pseudo_random_ids_values != annotations.get_ids(
#         Filter(random_values=10)
#     )
#
#     assert expected_pseudo_random_ids_values == annotations.get_ids(
#         Filter(pseudo_random_values=10)
#     )
