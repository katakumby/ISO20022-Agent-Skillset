---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Impact the Securities Position"]
content_origin: "source-transcription"
---

# Changes That Do Impact the Securities Position

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Securities Financing / Securities Financing Modification / Changes That Do Impact the Securities Position.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P383** Changes That Do Impact the Securities Position

**P384** This refers to the substitution, top up and withdrawal flows that per SMPG current market practice are considered as simple position movements for which settlement instructions are used. Despite the scenarios will cover pure settlement movements, upon settlement of the change of positions not only a SecuritiesSettlementTransactionConfirmation will be sent out but also a Securities Financing Status Advice to advise of the position change impacting the securities financing transaction.

**P385** Three Parties

**P386** A – Substitution

**P387** The securities financing instructing party (a broker) sends two SecuritiesSettlementTransactionInstruction (receipt free and deliver free) to the Securities Financing servicing party (a custodian) to substitute the quantity of securities A with securities B.

**P388** The securities financing servicing party in turn sends two SecuritiesSettlementTransactionInstruction (receipt free and deliver free) to the settlement executing party (a CSD).

**P389** The settlement executing party may send a status on the receipt and the delivery to the securities financing servicing party with two SecuritiesSettlementTransactionStatusAdvice.

**P390** The securities financing servicing party may in turn send a status on the receipt and the delivery to the securities financing instructing party with two SecuritiesSettlementTransactionStatusAdvice.

**P391** When the substitution is completed, the settlement executing party sends two SecuritiesSettlementTransactionConfirmation for the receipt and the delivery to the securities financing servicing party.

**P392** The securities financing servicing party in turn sends two SecuritiesSettlementTransactionConfirmation for the receipt and the delivery to the securities financing instructing party .

**P393** The securities financing servicing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

[fig-0044 - original figure evidence](../diagrams/fig-0044.md)

**P395** B – Top Up

**P396** The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (deliver free) to the securities financing servicing party (a custodian) to increase the quantity of securities that serves as collateral.

**P397** The securities financing servicing party in turn sends a SecuritiesSettlementTransactionInstruction (deliver free) to the settlement executing party (a CSD).

**P398** The settlement executing party may send a status on the delivery to the securities financing servicing party with a SecuritiesSettlementTransactionStatusAdvice.

**P399** The securities financing servicing party may in turn send a status on the delivery to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**P400** When the top up is completed, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation for the delivery to the securities financing servicing party.

**P401** The securities financing servicing party in turn sends a SecuritiesSettlementTransactionConfirmation for the delivery to the securities financing instructing party.

**P402** The securities financing servicing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

[fig-0045 - original figure evidence](../diagrams/fig-0045.md)

**P404** C – Withdrawal

**P405** The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (receipt free) to the securities financing servicing party (a custodian) to decrease the quantity of securities that serves as collateral.

**P406** The securities financing servicing party in turn sends a SecuritiesSettlementTransactionInstruction (receipt free) to the settlement executing party (a CSD).

**P407** The settlement executing party may send a status on the receipt to the Securities Financing servicing party with a

**P408** SecuritiesSettlementTransactionStatusAdvice.

**P409** The securities financing servicing party may in turn send a status on the receipt to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**P410** When the withdrawal is completed, the settlement executing party sends a

**P411** SecuritiesSettlementTransactionConfirmation for the receipt to the securities financing servicing party.

**P412** The securities financing servicing party in turn sends a SecuritiesSettlementTransactionConfirmation for the receipt to the securities financing instructing party.

**P413** The securities financing servicing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

[fig-0046 - original figure evidence](../diagrams/fig-0046.md)

**P415** Two Parties

**P416** A – Substitution

**P417** The securities financing instructing party (a broker) sends two SecuritiesSettlementTransactionInstruction (receipt free and deliver free) to the securities financing servicing party/settlement executing party (a sub custodian) to substitute the a quantity of securities. The securities financing servicing party/settlement executing party may send a status on the receipt and the delivery to the securities financing instructing party with two SecuritiesSettlementTransactionStatusAdvice.

**P418** When the substitution is completed, the securities financing servicing party/settlement executing party sends two SecuritiesSettlementTransactionConfirmation for the receipt and the delivery to the securities financing instructing party.

**P419** The securities financing servicing party/settlement executing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

[fig-0047 - original figure evidence](../diagrams/fig-0047.md)

**P421** B – Top Up

**P422** The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (deliver free) to the securities financing servicing party/settlement executing party (a sub-custodian) to increase the quantity of securities that serves as collateral.

**P423** The securities financing servicing party/settlement executing party may send a status on the delivery to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**P424** When the top up is completed, the securities financing servicing party/settlement executing party sends a

**P425** SecuritiesSettlementTransactionConfirmation for the delivery to the securities financing instructing party with a SecuritiesSettlementTransactionConfirmation.

**P426** The securities financing servicing party/settlement executing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

[fig-0048 - original figure evidence](../diagrams/fig-0048.md)

**P429** C – Withdrawal

**P430** The securities financing instructing party (a broker) sends a SecuritiesSettlementTransactionInstruction (receipt free) to the securities financing servicing party/settlement executing party (a sub-custodian) to decrease the quantity of securities that serve as collateral.

**P431** The securities financing servicing party/settlement executing party may send a status on the receipt to the securities financing instructing party with a SecuritiesSettlementTransactionStatusAdvice.

**P432** When the withdrawal is completed, the securities financing servicing party/settlement executing party sends a SecuritiesSettlementTransactionConfirmation for the receipt, to the securities financing instructing party.

**P433** The securities financing servicing party/settlement executing party will also send a SecuritiesFinancingStatusAdvice to the securities financing instructing party to advise of the position change impacting the securities financing transaction.

[fig-0049 - original figure evidence](../diagrams/fig-0049.md)

