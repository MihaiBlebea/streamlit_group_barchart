import {
	StreamlitComponentBase,
	withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend,
} from "chart.js"
import { Bar } from "react-chartjs-2"


ChartJS.register(
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend
)

interface Dataset {
	label: string
	background_color: string
	border_color: string
	data: Array<number>
}

class GroupBarchart extends StreamlitComponentBase {
	public state = {}

	private groups : Array<string> = this.props.args["groups"]
	private datasets : Array<Dataset> = this.props.args["datasets"]

	private formatDatasets = () => {
		return this.datasets.map((dataset)=> {
			return {
				label: dataset.label,
				backgroundColor: dataset.background_color,
				borderColor: dataset.border_color,
				borderWidth: 1,
				data: dataset.data
			}
		})
	}

	public chartData = {
		labels: this.groups,
		datasets: this.formatDatasets()
	}

	private options = {
		responsive: true,
		maintainAspectRatio: false,
		plugins: {
			tooltip: {
				enabled: true
			},
		},
		legend: {
			position: "top"
		}
	}

	private onClick = (event : any) => {
		event.persist()
		console.log(event)
	}

	public render = (): ReactNode => {
		return (
			<Bar 
				options={this.options} 
				data={this.chartData}
				onClick={this.onClick}
				onTouchStart={this.onClick}
			/>
		)
	}
}

export default withStreamlitConnection(GroupBarchart)
