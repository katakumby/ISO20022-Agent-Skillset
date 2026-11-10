---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessProcess Description", "BusinessProcess Diagram"]
content_origin: "source-transcription"
---

# BusinessProcess Diagram

Source: [src-000052](../../../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Locator: heading path BusinessProcess Description / BusinessProcess Diagram.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P108** BusinessProcess Diagram

**P109** This diagram pictures the high level BusinessProcesses covered by this project. These high level BusinessProcesses, if necessary, can be further split down into more detailed BusinessProcesses during the business modelling phase. The aim of the below is to describe the high-level scope of the project, not to be exhaustive. Some of the processes below (Collateral Management and Reporting processes) are shown for completeness purposes only but are not part of the scope of the Clearing project.

[fig-0002 - original figure evidence](../diagrams/fig-0002.md)

**P113** Trade Management process:

**P114** Definition: Process by which the CCP creates two trades (after Novation) from the one received from the exchange and reports them to the Clearing Members (CMs). The Novation is the legal concept that enables a CCP to become the counterparty. Through novation the original contract between the buyer and seller is extinguished and replaced by two new contracts, one between the CCP and the buyer and the one between the CCP and the seller.

**P115** Trigger: The process is triggered when the trading venue (either an exchange of a multilateral trading facility) notifies a trade to the CCP.

**P116** Pre-conditions: CCP accepts the trade.

**P117** Post-conditions: The Clearing member is notified of the trade.

**P118** Role: CCP

**P119** Risk Management process:

**P120** Definition: Process or approach that seeks to eliminate or at least minimize the level of risk associated with a business operation. This process encompasses three sub-processes: the netting, the margining and the Default Fund contribution processes.

**P121** Trigger: During the day or at the end of the day, depending on each CCP’s internal rules, each clearing member ‘risk profile is evaluated.

**P122** Pre-conditions: None.

**P123** Post-conditions:  Each Clearing Member may be requested to provide collateral to cover any risk identified.

**P124** Role: CCP

**P125** Netting process:

**P126** Definition: Process by which a CCP takes all trades legs of a CM into account to calculate the net resulting position (client and house) which will be the basis for the margining process.

**P127** Trigger: End of day milestones from all markets.

**P128** Pre-conditions: None

**P129** Post-conditions: The CCP nets all the positions (per margin account– House and Client). The Clearing Member is informed of the netting results and it reconciles his netting calculation with the CCP results (based on the netting parameters).

**P130** Role: CCP

**P131** Margining process: 

**P132** Definition: Process by which a CCP will collect margin from Clearing Members based on historical and current market value of securities held. If requirements are modified, margin calls are made to maintain the risk profile. Margin calls should be made at least once a day, intraday margin calls are possible. Margining requirements can be collected based on either net or gross positions held by a participant.

**P133** Trigger: The process can be triggered by the completion of the netting process, but margin calculation can be done intraday. Each CCP will define when this calculation should be done.

**P134** Pre-conditions: Net position has been calculated or a specific milestone is reached.

**P135** Post-conditions: CCP sends a margin call to Clearing Member if required.

**P136** Role: CCP

**P137** Default Fund Contribution process:

**P138** Definition: CCPs require participants to post assets in a clearing fund that can be used in the event of a default by a participant to compensate non-defaulting participants for losses they suffer due to this default. Contributions are linked to the riskiness of a participants’ activity as measured by margin posted, by size of position or sometimes by stress-testing results.

**P139** Trigger: Participant risk level assessment.

**P140** Pre-conditions: None

**P141** Post-conditions: CCP sends a margin call to Clearing Member if required.

**P142** Role: CCP

**P143** Collateral Management process (out of scope):

**P144** Definition: Process by which CCPs and CMs manage collateral positions during the transaction processing to ensure the risk is mitigated. CCPs also set the rules for the substitution of collateral; indeed substitution can be done under specific rules defined by the CCP (for example, type of new collateral, concentration limits).

**P145** Trigger: Calculation of the risk encountered by the CCP.

**P146** Pre-conditions: Postings of collateral to cover the risk of default of the Clearing Member.

**P147** Post-conditions: Movement on the clearing member collateral account.

**P148** Role: CCP

**P149** Settlement Management process:

**P150** Definition: The process of managing the correct settlement of the net open position of each clearing member. This process encompasses two sub-processes: the Settlement Netting process, the Buy-In process.

**P151** Trigger: End of day milestones from all markets.

**P152** Pre-conditions: The netting and margining processes are completed.

**P153** Post-conditions: None

**P154** Role: CCP

**P155** Settlement Netting process:

**P156** Definition: Process by which a CCP takes all trades legs of a CM into account and calculate the net resulting instruction (based on the CCP rules) that should be settled.

**P157** Trigger: The trades netting is completed and, based on the settlement results received from the Central Securities Depository, the CCP updates the positions/instructions (CNS model only). It may also apply the announced corporate events to the impacted positions/instructions (this process is out of scope).

**P158** Pre-conditions: None

**P159** Post-conditions: Settlement Obligation is sent to each Clearing Member.

**P160** Role: CCP

**P161** Buy-In process:

**P162** Definition: Process by which the CCP buy-in stocks to cover failed transactions.

**P163** Trigger: Non settlement of a trade after a certain number of days (depending on CCPs’).

**P164** Pre-conditions: The Clearing Member is not able to settle the trade(s).

**P165** Post-conditions: Settlement of the trade.

**P166** Role: CCP

**P167** Reporting process (Out of scope):

**P168** Definition: Process by which CCPs provide reports on cash settlement information, on trade(s) that did not settle correctly at the settlement date, or on the valuation of the collateral posted by the clearing members.

**P169** Trigger: End of day milestones from all markets.

**P170** Pre-conditions: The CCP has received the report with all failed trades from the Central Securities Depository or the end of day process has generated reports that are sent out to the clearing members.

**P171** Post-conditions: None

**P172** Role: CCP

**P175**   


