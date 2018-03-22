import pandas as pd
import pytest  # pylint: disable=unused-import

import calliope
from calliope.core.time import clustering, funcs, masks


class TestMasks:
    @pytest.fixture
    def model_national(self):
        return calliope.examples.national_scale(
            override_dict={'model.subset_time': ['2005-01-01', '2005-01-31']}
        )

    @pytest.fixture
    def model_urban(self):
        return calliope.examples.urban_scale(
            override_dict={'model.subset_time': ['2005-01-01', '2005-01-31']}
        )

    def test_zero(self, model_national):
        data = model_national._model_data_original.copy()
        mask = masks.zero(data, 'csp', var='resource')

        dtindex = pd.DatetimeIndex([
            '2005-01-01 00:00:00', '2005-01-01 01:00:00',
            '2005-01-01 02:00:00', '2005-01-01 03:00:00',
            '2005-01-01 04:00:00', '2005-01-01 05:00:00',
            '2005-01-01 06:00:00', '2005-01-01 16:00:00',
            '2005-01-01 17:00:00', '2005-01-01 18:00:00',
            '2005-01-01 19:00:00', '2005-01-01 20:00:00',
            '2005-01-01 21:00:00', '2005-01-01 22:00:00',
            '2005-01-01 23:00:00', '2005-01-02 00:00:00',
            '2005-01-02 01:00:00', '2005-01-02 02:00:00',
            '2005-01-02 03:00:00', '2005-01-02 04:00:00',
            '2005-01-02 05:00:00', '2005-01-02 06:00:00',
            '2005-01-02 16:00:00', '2005-01-02 17:00:00',
            '2005-01-02 18:00:00', '2005-01-02 19:00:00',
            '2005-01-02 20:00:00', '2005-01-02 21:00:00',
            '2005-01-02 22:00:00', '2005-01-02 23:00:00',
            '2005-01-03 00:00:00', '2005-01-03 01:00:00',
            '2005-01-03 02:00:00', '2005-01-03 03:00:00',
            '2005-01-03 04:00:00', '2005-01-03 05:00:00',
            '2005-01-03 06:00:00', '2005-01-03 16:00:00',
            '2005-01-03 17:00:00', '2005-01-03 18:00:00',
            '2005-01-03 19:00:00', '2005-01-03 20:00:00',
            '2005-01-03 21:00:00', '2005-01-03 22:00:00',
            '2005-01-03 23:00:00', '2005-01-04 00:00:00',
            '2005-01-04 01:00:00', '2005-01-04 02:00:00',
            '2005-01-04 03:00:00', '2005-01-04 04:00:00',
            '2005-01-04 05:00:00', '2005-01-04 06:00:00',
            '2005-01-04 16:00:00', '2005-01-04 17:00:00',
            '2005-01-04 18:00:00', '2005-01-04 19:00:00',
            '2005-01-04 20:00:00', '2005-01-04 21:00:00',
            '2005-01-04 22:00:00', '2005-01-04 23:00:00',
            '2005-01-05 00:00:00', '2005-01-05 01:00:00',
            '2005-01-05 02:00:00', '2005-01-05 03:00:00',
            '2005-01-05 04:00:00', '2005-01-05 05:00:00',
            '2005-01-05 06:00:00', '2005-01-05 16:00:00',
            '2005-01-05 17:00:00', '2005-01-05 18:00:00',
            '2005-01-05 19:00:00', '2005-01-05 20:00:00',
            '2005-01-05 21:00:00', '2005-01-05 22:00:00',
            '2005-01-05 23:00:00'])

        assert dtindex.equals(mask[0:75])

    def test_extreme(self, model_national):
        data = model_national._model_data_original.copy()
        mask = masks.extreme(
            data, 'csp', var='resource', how='max',
            length='2D', n=1, padding='2H'
        )

        dtindex = pd.DatetimeIndex([
            '2005-01-18 22:00:00', '2005-01-18 23:00:00',
            '2005-01-19 00:00:00', '2005-01-19 01:00:00',
            '2005-01-19 02:00:00', '2005-01-19 03:00:00',
            '2005-01-19 04:00:00', '2005-01-19 05:00:00',
            '2005-01-19 06:00:00', '2005-01-19 07:00:00',
            '2005-01-19 08:00:00', '2005-01-19 09:00:00',
            '2005-01-19 10:00:00', '2005-01-19 11:00:00',
            '2005-01-19 12:00:00', '2005-01-19 13:00:00',
            '2005-01-19 14:00:00', '2005-01-19 15:00:00',
            '2005-01-19 16:00:00', '2005-01-19 17:00:00',
            '2005-01-19 18:00:00', '2005-01-19 19:00:00',
            '2005-01-19 20:00:00', '2005-01-19 21:00:00',
            '2005-01-19 22:00:00', '2005-01-19 23:00:00',
            '2005-01-20 00:00:00', '2005-01-20 01:00:00',
            '2005-01-20 02:00:00', '2005-01-20 03:00:00',
            '2005-01-20 04:00:00', '2005-01-20 05:00:00',
            '2005-01-20 06:00:00', '2005-01-20 07:00:00',
            '2005-01-20 08:00:00', '2005-01-20 09:00:00',
            '2005-01-20 10:00:00', '2005-01-20 11:00:00',
            '2005-01-20 12:00:00', '2005-01-20 13:00:00',
            '2005-01-20 14:00:00', '2005-01-20 15:00:00',
            '2005-01-20 16:00:00', '2005-01-20 17:00:00',
            '2005-01-20 18:00:00', '2005-01-20 19:00:00',
            '2005-01-20 20:00:00', '2005-01-20 21:00:00',
            '2005-01-20 22:00:00', '2005-01-20 23:00:00',
            '2005-01-21 00:00:00', '2005-01-21 01:00:00'])

        assert dtindex.equals(mask)

    def test_extreme_diff_and_normalize(self, model_urban):
        data = model_urban._model_data_original.copy()
        mask = masks.extreme_diff(
            data, 'demand_heat', 'demand_electricity',
            var='resource', how='min',
            length='1D', n=2, normalize=True
        )

        dtindex = pd.DatetimeIndex([
            '2005-01-13 00:00:00', '2005-01-13 01:00:00',
            '2005-01-13 02:00:00', '2005-01-13 03:00:00',
            '2005-01-13 04:00:00', '2005-01-13 05:00:00',
            '2005-01-13 06:00:00', '2005-01-13 07:00:00',
            '2005-01-13 08:00:00', '2005-01-13 09:00:00',
            '2005-01-13 10:00:00', '2005-01-13 11:00:00',
            '2005-01-13 12:00:00', '2005-01-13 13:00:00',
            '2005-01-13 14:00:00', '2005-01-13 15:00:00',
            '2005-01-13 16:00:00', '2005-01-13 17:00:00',
            '2005-01-13 18:00:00', '2005-01-13 19:00:00',
            '2005-01-13 20:00:00', '2005-01-13 21:00:00',
            '2005-01-13 22:00:00', '2005-01-13 23:00:00',
            '2005-01-19 00:00:00', '2005-01-19 01:00:00',
            '2005-01-19 02:00:00', '2005-01-19 03:00:00',
            '2005-01-19 04:00:00', '2005-01-19 05:00:00',
            '2005-01-19 06:00:00', '2005-01-19 07:00:00',
            '2005-01-19 08:00:00', '2005-01-19 09:00:00',
            '2005-01-19 10:00:00', '2005-01-19 11:00:00',
            '2005-01-19 12:00:00', '2005-01-19 13:00:00',
            '2005-01-19 14:00:00', '2005-01-19 15:00:00',
            '2005-01-19 16:00:00', '2005-01-19 17:00:00',
            '2005-01-19 18:00:00', '2005-01-19 19:00:00',
            '2005-01-19 20:00:00', '2005-01-19 21:00:00',
            '2005-01-19 22:00:00', '2005-01-19 23:00:00'])

        assert dtindex.equals(mask)

    def test_week(self, model_national):
        data = model_national._model_data_original.copy()
        mask = masks.week(
            data, 'extreme',
            tech='csp', var='resource', how='max',
            length='2D', n=1,
        )

        dtindex_start = pd.DatetimeIndex([
            '2005-01-15 00:00:00', '2005-01-15 01:00:00',
            '2005-01-15 02:00:00', '2005-01-15 03:00:00',
            '2005-01-15 04:00:00', '2005-01-15 05:00:00',
            '2005-01-15 06:00:00', '2005-01-15 07:00:00',
            '2005-01-15 08:00:00', '2005-01-15 09:00:00'])
        dtindex_end = pd.DatetimeIndex([
            '2005-01-22 14:00:00', '2005-01-22 15:00:00',
            '2005-01-22 16:00:00', '2005-01-22 17:00:00',
            '2005-01-22 18:00:00', '2005-01-22 19:00:00',
            '2005-01-22 20:00:00', '2005-01-22 21:00:00',
            '2005-01-22 22:00:00', '2005-01-22 23:00:00'])

        assert dtindex_start.equals(mask[:10])
        assert dtindex_end.equals(mask[-10:])
