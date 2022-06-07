const time = new Date();
import {undergrad_intervals, indicator_to_change} from './config.mjs';

const card = {
	metadata: {
		topic: "topic",
		state: "postgrad",
		confidence: 250,
		interval: 345600,
		last_reviewed: 1638451223,
		next_review: 1638796823,
		last_review_indicator: "4"
	},
	question: "Q1",
	answer: "A1"
}

console.log(card)

function process_undergrad_card(card, indication) {

	/*if (card["metadata"]["last_review_indicator"] == "3" and indication == "3") or indication == "4":
		card["metadata"]["state"] = "postgrad"

	time_reviewed = round(time.time())

	card["metadata"]["last_reviewed"] = time_reviewed
	card["metadata"]["interval"] = config.indicator_to_change[indication]["new_interval"]
	card["metadata"]["next_review"] = time_reviewed + card["metadata"]["interval"]

	card["metadata"]["last_review_indicator"] = indication

	return card*/

	if ((card["metadata"]["last_review_indicator"] == "3" && indication == "3") || indication == "4"){
		card["metadata"]["state"] = "postgrad";
	}

	let time_reviewed = Math.round(time.getTime());

	card["metadata"]["time_reviewed"] = time_reviewed;
	card["metadata"]["interval"] = indicator_to_change[indication]["new_interval"];
	card["metadata"]["next_review"] = time_reviewed + card["metadata"]["interval"];

	card["metadata"]["last_review_indicator"] = indication;

	return card;
}
let processedCard = process_undergrad_card(card,"1")
console.log(processedCard)

function process_postgrad_card(card, indication){
    /*time_reviewed = round(time.time())
    
    card["metadata"]["last_reviewed"] = time_reviewed
    card["metadata"]["next_review"] = time_reviewed + card["metadata"]["interval"]

    if indication == "1":
        card["metadata"]["state"] == "undergrad"
        card["metadata"]["interval"] = config.indicator_to_change[indication]["new_interval"]
    else:
        card["metadata"]["interval"] = card["metadata"]["interval"] * (card["metadata"]["confidence"] / 100)

    card["metadata"]["confidence"] = card["metadata"]["confidence"] * config.indicator_to_change[indication]["confidence_percentage_change_result"]

    return card*/

	let time_reviewed = Math.round(time.getTime());

	card["metadata"]["last_reviewed"] = time_reviewed;
	card["metadata"]["next_review"] = time_reviewed + card["metadata"]["interval"];

	if (indication == 1){
		card["metadata"]["state"] = "undergrad";
		card["metadata"]["interval"] = indicator_to_change[indication]["new_interval"];
	}
	else{
		card["metadata"]["interval"] = card["metadata"]["interval"] * (card["metadata"]["confidence"] / 100);
	}

	card["metadata"]["confidence"] = card["metadata"]["confidence"] * indicator_to_change[indication]["confidence_percentage_change_result"];
	return card;
}

processedCard = process_postgrad_card(card,1);
console.log(processedCard);