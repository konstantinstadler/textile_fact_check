import pymrio
import matplotlib.pyplot as plt

# import hvplot.pandas

pymrio.download_exiobase3('./mriodata', years=2021)

pxp = pymrio.parse_exiobase3('./mriodata/IOT_2021_pxp.zip')

ixi = pymrio.parse_exiobase3('./mriodata/IOT_2021_ixi.zip')

pxp.calc_all()

pxp.Z.index.get_level_values('sector')[pxp.Z.index.get_level_values('sector').str.contains('apparel')]

clothes = 'Wearing apparel; furs (18)'
textiles = 'Textiles (17)'

co2 = 'Carbon dioxide (CO2) IPCC categories 1 to 4 and 6 to 7 (excl land use, land use change and forestry)'


at = pxp.impacts.D_cba.loc[co2, 'AT']

atu = pxp.impacts.unit.loc[co2]



atperc = (at / at.sum()) * 100

atperchead = atperc.sort_values(ascending=False).head(20)

atperchead.index = atperchead.index.str.slice(0,50)


# plt.style.use('seaborn-darkgrid')
plt.style.use('seaborn')

atperchead.plot(kind='barh', rot=45, ylabel = 'percent of' + co2, xlabel = 'Product sectors', title='Austrian consumption footprints\n Percent of total ' + co2)

# pxp.impacts.D_cba.loc[co2, 'AT'].sort_values(ascending=False).head(10).plot(kind='barh')

# plt.tight_layout()

plt.savefig('at_footprint.png')

plt.show()

total = pxp.aggregate( region_agg="global",)



.plot()


plt.show()


globco2 = total.impacts.D_cba.loc[co2, 'global']

totperc = (globco2 / globco2.sum()) * 100

globco2head = totperc.sort_values(ascending=False).head(20)

globco2head.index = globco2head.index.str.slice(0,50)

globco2head.plot(kind='barh', rot=45, ylabel = 'percent of' + co2, xlabel = 'Product sectors', title='Global footprints\n Percent of total ' + co2)

plt.savefig('total_footprint.png')

plt.show()


ixi = pymrio.parse_exiobase3('./mriodata/IOT_2021_ixi.zip')
ixi.calc_all()

totixi = pxp.aggregate( region_agg="global")

totixi.impacts.D_cba.loc[co2, 'global'].loc[textiles]
totixi.impacts.D_cba.loc[co2, 'global'].loc[clothes]

total_cba = totixi.impacts.D_cba.loc[co2, 'global'].loc[textiles] + totixi.impacts.D_cba.loc[co2, 'global'].loc[clothes]
total_cba_perc = 100 *total_cba / total_co2

total_co2 = totixi.impacts.D_cba.loc[co2].sum()


totixi.impacts.D_pba.loc[co2, 'global'].loc[textiles]
totixi.impacts.D_pba.loc[co2, 'global'].loc[clothes]

total_pba = totixi.impacts.D_pba.loc[co2, 'global'].loc[textiles] + totixi.impacts.D_pba.loc[co2, 'global'].loc[clothes]

total_pba_perc = 100 *total_pba / total_co2



totixiperc = (totixi.impacts.D_cba.loc[co2,'global'] / total_co2) * 100

totixiperchead = totixiperc.sort_values(ascending=False).head(40)

totixiperchead.index = totixiperchead.index.str.slice(0,50)

totixiperchead.plot(kind='barh', rot=25, ylabel = 'percent of' + co2, xlabel = 'Industry sectors', title='Global CO2 emissions \n Percent of total')

plt.show()

