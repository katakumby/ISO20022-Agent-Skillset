---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.016.001.05"
message_family: "setr.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.016.001.05"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "56 setr.016.001.05 OrderInstructionStatusReportV05", "file_pages": [4109, 4204]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# setr.016.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 56 setr.016.001.05 OrderInstructionStatusReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp4109–4204; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 56 setr.016.001.05 OrderInstructionStatusReportV05, Functionality, file p4109.**

Scope
The OrderInstructionStatusReport message is sent by an executing party, for example, a transfer agent,
to the instructing party, for example, an investment manager or its authorised representative, to report
the status of an order from the time the executing party receives the order until the time the order is
executed.
Usage
The OrderInstructionStatusReport message is used to report on the status of a subscription, redemption
or a switch order.
The OrderInstructionStatusReport message may be used to give the status of:
- one order message by using OrderDetailsReport or,
- one or more individual order instructions by using IndividualOrderDetailsReport, or
- one or more switch orders by using SwitchOrderDetailsReport.
If the OrderInstructionStatusReport message is used to report the status of an individual order, then
IndividualOrderDetailsReport is used and the order reference of the individual order is quoted in
OrderReference. The message identification of the message in which the individual order was
conveyed may also be quoted in RelatedReference but this is not recommended.
If the OrderInstructionStatusReport message is used to report the status of a switch order, then
SwitchOrderDetailsReport is used and the order reference of the switch order is quoted in
OrderReference. The message identification of the message in which the switch order was conveyed
may also be quoted in RelatedReference but this is not recommended.
If the OrderInstructionStatusReport message is used to report the status of an entire order message, for
example, the SubscriptionBulkOrder, or a SubscriptionOrder containing several orders, then
OrderDetailsReport is used and the message identification of the order message is quoted in
RelatedReference. All the orders within the message must have the same status.
One of the following statuses can be reported:
- an accepted status, or,
- an already executed status, or,
- a sent to next party status, or,
- a received status, or,
- a settled status, or,
- a communication problem with next party status, or,
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4109 May 2026

**src-000096, 56 setr.016.001.05 OrderInstructionStatusReportV05, Functionality, file p4110.**

- a confirmation amendment status, or,
- a done for the day status, or,
- a partially done status, or,
- an open status, or,
- a cancelled status, or
- a conditionally accepted status, or,
- a rejected status, or,
- a suspended status, or,
- a partially settled status, or,
- an in-repair status (only for an individual or switch order).
For a switch order, the OrderInstructionStatusReport message provides the status of the whole switch
order, that is, it is not possible to accept one leg and to reject the other leg: the entire switch order has
to be rejected. In order to identify the legs within the switch that are causing the problem, the leg is
identified in either the RedemptionLegIdentification or SubscriptionLegIdentification elements.
When the OrderInstructionStatusReport is used to give the status of an individual or a switch order, the
following can be specified:
- repaired conditions (for a switch, this is at the level of a leg),
- information related to the order, for example, settlement amount, number of units, expected trade
date.
Outline
The OrderInstructionStatusReportV05 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. Reference
Reference to the message or communication that was previously received.
C. StatusReport
Status of the order.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4110 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [56 setr.016.001.05 OrderInstructionStatusReportV05](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02937.md) | 4109–4110 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02938.md) | 4111–4116 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02939.md) | 4117–4118 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02940.md) | 4119–4126 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02941.md) | 4127–4127 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt; / 56.4.3.1.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02942.md) | 4128–4128 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt; / 56.4.3.1.2 OrderStatus &lt;OrdrSts&gt; / 56.4.3.1.2.1 Status &lt;Sts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02943.md) | 4129–4129 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt; / 56.4.3.1.2 OrderStatus &lt;OrdrSts&gt; / 56.4.3.1.2.2 Cancelled &lt;Canc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02944.md) | 4130–4130 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt; / 56.4.3.1.2 OrderStatus &lt;OrdrSts&gt; / 56.4.3.1.2.4 Rejected &lt;Rjctd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02945.md) | 4131–4133 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt; / 56.4.3.1.2 OrderStatus &lt;OrdrSts&gt; / 56.4.3.1.2.4 Rejected &lt;Rjctd&gt; / 56.4.3.1.2.4.1 Reason &lt;Rsn&gt; / 56.4.3.1.2.4.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02946.md) | 4134–4134 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.1 OrderDetailsReport &lt;OrdrDtlsRpt&gt; / 56.4.3.1.3 StatusInitiator &lt;StsInitr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02947.md) | 4135–4138 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02948.md) | 4139–4139 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.5 NonceIdentification &lt;NonceId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02949.md) | 4140–4140 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.2.7.2 Cancelled &lt;Canc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02950.md) | 4141–4141 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.2.7.3 ConditionallyAccepted &lt;CondlyAccptd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02951.md) | 4142–4142 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.2.7.4 Rejected &lt;Rjctd&gt; / 56.4.3.2.7.4.1 Reason &lt;Rsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02952.md) | 4143–4144 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.2.7.4 Rejected &lt;Rjctd&gt; / 56.4.3.2.7.4.1 Reason &lt;Rsn&gt; / 56.4.3.2.7.4.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02953.md) | 4145–4145 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.2.7.4 Rejected &lt;Rjctd&gt; / 56.4.3.2.7.4.2 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02954.md) | 4146–4146 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.2.7.7 PartiallySettled &lt;PrtlySttld&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02955.md) | 4147–4147 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.8 RepairedFee &lt;RprdFee&gt; / 56.4.3.2.8.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02956.md) | 4148–4149 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.8 RepairedFee &lt;RprdFee&gt; / 56.4.3.2.8.1 Type &lt;Tp&gt; / 56.4.3.2.8.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02957.md) | 4150–4150 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.8 RepairedFee &lt;RprdFee&gt; / 56.4.3.2.8.5 RepairedDiscountRate &lt;RprdDscntRate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02958.md) | 4151–4151 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.8 RepairedFee &lt;RprdFee&gt; / 56.4.3.2.8.8 CommercialAgreementReference &lt;ComrclAgrmtRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02959.md) | 4152–4153 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.1 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02960.md) | 4154–4154 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.1 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 56.4.3.2.10.1.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02961.md) | 4155–4155 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.1 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 56.4.3.2.10.1.5 AccountServicer &lt;AcctSvcr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02962.md) | 4156–4156 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.1 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 56.4.3.2.10.1.8 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02963.md) | 4157–4158 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.2 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.2.10.2.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02964.md) | 4159–4159 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.2 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.2.10.2.1 Identification &lt;Id&gt; / 56.4.3.2.10.2.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02965.md) | 4160–4160 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.2 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.2.10.2.1 Identification &lt;Id&gt; / 56.4.3.2.10.2.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02966.md) | 4161–4161 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.2 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.2.10.2.1 Identification &lt;Id&gt; / 56.4.3.2.10.2.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 56.4.3.2.10.2.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02967.md) | 4162–4162 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.2 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.2.10.2.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02968.md) | 4163–4163 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.2 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.2.10.2.9 SeriesIdentification &lt;SrsId&gt; / 56.4.3.2.10.2.9.1 SeriesDate &lt;SrsDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02969.md) | 4164–4164 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.6 GrossAmount &lt;GrssAmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02970.md) | 4165–4165 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.10 OrderData &lt;OrdrData&gt; / 56.4.3.2.10.9 UnitCurrency &lt;UnitCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02971.md) | 4166–4166 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.11 NewDetails &lt;NewDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02972.md) | 4167–4167 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.12 GatingOrHoldBackDetails &lt;GtgOrHldBckDtls&gt; / 56.4.3.2.12.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02973.md) | 4168–4168 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.12 GatingOrHoldBackDetails &lt;GtgOrHldBckDtls&gt; / 56.4.3.2.12.2 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02974.md) | 4169–4169 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.12 GatingOrHoldBackDetails &lt;GtgOrHldBckDtls&gt; / 56.4.3.2.12.4 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 56.4.3.2.12.4.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02975.md) | 4170–4170 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.12 GatingOrHoldBackDetails &lt;GtgOrHldBckDtls&gt; / 56.4.3.2.12.4 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 56.4.3.2.12.4.3 CUSIP &lt;CUSIP&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02976.md) | 4171–4171 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.12 GatingOrHoldBackDetails &lt;GtgOrHldBckDtls&gt; / 56.4.3.2.12.4 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 56.4.3.2.12.4.10 Dutch &lt;Dtch&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02977.md) | 4172–4172 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.2 IndividualOrderDetailsReport &lt;IndvOrdrDtlsRpt&gt; / 56.4.3.2.12 GatingOrHoldBackDetails &lt;GtgOrHldBckDtls&gt; / 56.4.3.2.12.4 FinancialInstrumentIdentification &lt;FinInstrmId&gt; / 56.4.3.2.12.4.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 56.4.3.2.12.4.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02978.md) | 4173–4175 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02979.md) | 4176–4176 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.4 DealReference &lt;DealRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02980.md) | 4177–4177 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.3.7.2 Cancelled &lt;Canc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02981.md) | 4178–4178 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.3.7.3 ConditionallyAccepted &lt;CondlyAccptd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02982.md) | 4179–4179 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.3.7.4 Rejected &lt;Rjctd&gt; / 56.4.3.3.7.4.1 Reason &lt;Rsn&gt; / 56.4.3.3.7.4.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02983.md) | 4180–4181 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.3.7.4 Rejected &lt;Rjctd&gt; / 56.4.3.3.7.4.1 Reason &lt;Rsn&gt; / 56.4.3.3.7.4.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02984.md) | 4182–4182 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.7 OrderStatus &lt;OrdrSts&gt; / 56.4.3.3.7.4 Rejected &lt;Rjctd&gt; / 56.4.3.3.7.4.2 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02985.md) | 4183–4183 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02986.md) | 4184–4185 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.1 LegIdentification &lt;LegId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02987.md) | 4186–4186 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.1 LegIdentification &lt;LegId&gt; / 56.4.3.3.8.1.1 RedemptionLegIdentification &lt;RedLegId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02988.md) | 4187–4187 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.3 RepairedFee &lt;RprdFee&gt; / 56.4.3.3.8.3.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02989.md) | 4188–4189 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.3 RepairedFee &lt;RprdFee&gt; / 56.4.3.3.8.3.1 Type &lt;Tp&gt; / 56.4.3.3.8.3.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02990.md) | 4190–4190 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.3 RepairedFee &lt;RprdFee&gt; / 56.4.3.3.8.3.5 RepairedDiscountRate &lt;RprdDscntRate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02991.md) | 4191–4191 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.3 RepairedFee &lt;RprdFee&gt; / 56.4.3.3.8.3.8 CommercialAgreementReference &lt;ComrclAgrmtRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02992.md) | 4192–4192 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.4 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 56.4.3.3.8.4.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02993.md) | 4193–4193 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.4 InvestmentAccountDetails &lt;InvstmtAcctDtls&gt; / 56.4.3.3.8.4.6 OrderOriginatorEligibility &lt;OrdrOrgtrElgblty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02994.md) | 4194–4194 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02995.md) | 4195–4196 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.3.8.5.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02996.md) | 4197–4197 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.3.8.5.1 Identification &lt;Id&gt; / 56.4.3.3.8.5.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02997.md) | 4198–4198 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.3.8.5.1 Identification &lt;Id&gt; / 56.4.3.3.8.5.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02998.md) | 4199–4199 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.3.8.5.1 Identification &lt;Id&gt; / 56.4.3.3.8.5.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 56.4.3.3.8.5.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-02999.md) | 4200–4200 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.3.8.5.6 SecuritiesForm &lt;SctiesForm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03000.md) | 4201–4201 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.8 LegInformation &lt;LegInf&gt; / 56.4.3.3.8.5 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 56.4.3.3.8.5.9 SeriesIdentification &lt;SrsId&gt; / 56.4.3.3.8.5.9.1 SeriesDate &lt;SrsDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03001.md) | 4202–4202 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.3.3 SwitchOrderDetailsReport &lt;SwtchOrdrDtlsRpt&gt; / 56.4.3.3.11 NewDetails &lt;NewDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03002.md) | 4203–4203 |
| [56 setr.016.001.05 OrderInstructionStatusReportV05 / 56.4 Message Building Blocks / 56.4.4 Extension &lt;Xtnsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03003.md) | 4204–4204 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000095-beneficial-owner.md) | participant | src-000095 |
| [Concentrator](../../../../../shared/reference/participants/participant-src-000095-concentrator.md) | participant | src-000095 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000095-csd-icsd.md) | participant | src-000095 |
| [CSD](../../../../../shared/reference/participants/participant-src-000095-csd.md) | participant | src-000095 |
| [Custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md) | participant | src-000095 |
| [Distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md) | participant | src-000095 |
| [Executing Party / Registering Party](../../../../../shared/reference/participants/participant-src-000095-executing-party-registering-party.md) | participant | src-000095 |
| [Executing Party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | participant | src-000095 |
| [Fund Accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | participant | src-000095 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md) | participant | src-000095 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000095-icsd.md) | participant | src-000095 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000095-institutional-investor.md) | participant | src-000095 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | participant | src-000095 |
| [Intermediary](../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | participant | src-000095 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | participant | src-000095 |
| [Paying Agent](../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | participant | src-000095 |
| [Receiving Party (all levels)](../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md) | participant | src-000095 |
| [Reporting Party](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | participant | src-000095 |
| [Requesting Party](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | participant | src-000095 |
| [Transfer Agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | participant | src-000095 |
| [Transferee's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-executing-party.md) | participant | src-000095 |
| [Transferee's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md) | participant | src-000095 |
| [Transferor's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-executing-party.md) | participant | src-000095 |
| [Transferor's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md) | participant | src-000095 |
| [Account Administration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p185-account-administration.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p186-order-processing.md) | business-flow | src-000095 |
| [Order Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | business-flow | src-000095 |
| [Payment Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p188-payment-execution.md) | business-flow | src-000095 |
| [Payment Execution - Advance Pay In](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p189-payment-execution-advance-pay-in.md) | business-flow | src-000095 |
| [Payment Execution - Pay In Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p190-payment-execution-pay-in-arrears.md) | business-flow | src-000095 |
| [Payment Execution - Pay Out Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | business-flow | src-000095 |
| [Tax Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p192-tax-accounting.md) | business-flow | src-000095 |
| [Fund Valuation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p193-fund-valuation.md) | business-flow | src-000095 |
| [Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p194-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Transaction Based Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Trailer Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p196-commission-accounting-trailer-commission-accounting.md) | business-flow | src-000095 |
| [Reconciliation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p197-reconciliation.md) | business-flow | src-000095 |
| [Distribution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p199-distribution.md) | business-flow | src-000095 |
| [Registration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p200-registration.md) | business-flow | src-000095 |
| [Account Opening](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | business-flow | src-000095 |
| [Account Modification](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | business-flow | src-000095 |
| [Reporting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md) | business-flow | src-000095 |
| [Custody and Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | business-flow | src-000095 |
| [Transparency of Holdings](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | business-flow | src-000095 |
| [Stock Transfers (Single Leg Transfer)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Single Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | business-flow | src-000095 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
