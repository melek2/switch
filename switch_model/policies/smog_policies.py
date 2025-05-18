# switch_model/policies/smog_policies.py
from __future__ import division
import os
import switch_model.reporting as reporting

def define_components(model):
    # 
    # 
    pass

def load_inputs(model, switch_data, inputs_dir):
    # to read a smog_policies.csv with a per-period PM2.5 cap or cost,
    # we’d do something like:
    # switch_data.load_aug(
    #     filename=os.path.join(inputs_dir, "smog_policies.csv"),
    #     optional=True,
    #     optional_params=(model.smog_cap_g_per_yr, model.smog_cost_dollar_per_g),
    #     param=(model.smog_cap_g_per_yr, model.smog_cost_dollar_per_g),
    # )
    pass

def post_solve(model, outdir):
    """
    Export annual PM2.5 metrics to smog.csv, analogous to emissions.csv
    """
    def get_row(m, period):
        return [
            period,
            # total PM2.5 emitted in grams in that period:
            m.AnnualPM25[period],
            ## any cap or cost defined (if added in params)
            # m.smog_cap_g_per_yr[period],
            # m.smog_cost_dollar_per_g[period],
        ]

    reporting.write_table(
        model,
        model.PERIODS,
        output_file=os.path.join(outdir, "smog.csv"),
        headings=(
            "PERIOD",
            "AnnualPM25_g_per_yr",
            # "smog_cap_g_per_yr",
            # "smog_cost_dollar_per_g",
        ),
        values=get_row,
    )