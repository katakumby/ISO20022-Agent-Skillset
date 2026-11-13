---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.010.001.04"
message_family: "secl.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.010.001.04"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "11 MX secl.010.001.04 SettlementObligationReportV04", "file_pages": [316, 372]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.010.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 11 MX secl.010.001.04 SettlementObligationReportV04

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp316–372; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 11 MX secl.010.001.04 SettlementObligationReportV04, Functionality, file p316.**

Scope
The SettlementObligationReport message is sent by the central counterparty (CCP) to a clearing
member to report on the settlement obligation that will be submitted for settlement.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The SettlementObligationReport message may also be sent to a third party processing the settlement
obligation(s) on behalf of more than one clearing member.
The Settlement Obligation Report message is provided per delivery account and per instrument. The
report can be provided for one specific delivering party or one specific receiving party. It can also be
generated per non clearing member.
Outline
The SettlementObligationReportV04 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. ReportParameters
Provides details about the report such as the report identification, the creation date and time.
B. Pagination
Page number of the message (within a report) and continuation indicator to indicate that the report
is to continue or that the message is the last page of the report.
C. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
D. ClearingSegment
Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing
counterparty's clearing system. Indeed, Clearing Member Firms receive messages from the same
system (same sender) and this field allows them to know if the message is related to equities or
derivatives.
E. DeliveryAccount
Provides the identification of the account used for netting. This is an account opened by the central
counterparty in the name of the clearing member or its settlement agent within the account
structure, for settlement purposes (gives information about the clearing member/its settlement
agent account at the central securities depository).
F. ReportDetails
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 316

**src-000053, 11 MX secl.010.001.04 SettlementObligationReportV04, Functionality, file p317.**

Provides details on the settlement obligation report.
G. SettlementParties
Provides details about the receiving parties involved in the settlement chain.
H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 317

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 MX secl.010.001.04 SettlementObligationReportV04](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00242.md) | 316–317 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00243.md) | 318–320 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00244.md); [Constraints continuation C18–C19 (file p325)](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00245.md#file-page-325) | 321–324 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00245.md) | 325–325 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00246.md) | 326–326 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.5 DeliveryAccount &lt;DlvryAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00247.md) | 327–330 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.1 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00248.md) | 331–334 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.1 SettlementObligationIdentification &lt;SttlmOblgtnId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00249.md) | 335–335 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.3 IntendedSettlementDate &lt;IntnddSttlmDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00250.md) | 336–336 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.4 Quantity &lt;Qty&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00251.md) | 337–337 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.7 TradeDate &lt;TradDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00252.md) | 338–338 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.9 ClearingAccountType &lt;ClrAcctTp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00253.md) | 339–339 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.10 SafekeepingPlace &lt;SfkpgPlc&gt; / 11.4.6.2.10.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00254.md) | 340–340 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.10 SafekeepingPlace &lt;SfkpgPlc&gt; / 11.4.6.2.10.2 Country &lt;Ctry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00255.md) | 341–341 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.10 SafekeepingPlace &lt;SfkpgPlc&gt; / 11.4.6.2.10.3 TypeAndIdentification &lt;TpAndId&gt; / 11.4.6.2.10.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00256.md) | 342–342 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.11 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00257.md) | 343–343 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00258.md) | 344–345 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00259.md) | 346–347 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00260.md) | 348–348 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.2 Party1 &lt;Pty1&gt; / 11.4.6.2.14.1.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00261.md) | 349–349 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.2 Party1 &lt;Pty1&gt; / 11.4.6.2.14.1.2.5 SubAccount &lt;SubAcct&gt; / 11.4.6.2.14.1.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00262.md) | 350–350 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00263.md) | 351–351 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.3 Party2 &lt;Pty2&gt; / 11.4.6.2.14.1.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00264.md) | 352–352 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.3 Party2 &lt;Pty2&gt; / 11.4.6.2.14.1.3.5 SubAccount &lt;SubAcct&gt; / 11.4.6.2.14.1.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00265.md) | 353–353 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.6.2.14.1.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00266.md) | 354–355 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00267.md) | 356–356 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.2 Party1 &lt;Pty1&gt; / 11.4.6.2.14.2.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00268.md) | 357–357 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.2 Party1 &lt;Pty1&gt; / 11.4.6.2.14.2.2.5 SubAccount &lt;SubAcct&gt; / 11.4.6.2.14.2.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00269.md) | 358–358 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00270.md) | 359–359 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.3 Party2 &lt;Pty2&gt; / 11.4.6.2.14.2.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00271.md) | 360–360 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.3 Party2 &lt;Pty2&gt; / 11.4.6.2.14.2.3.5 SubAccount &lt;SubAcct&gt; / 11.4.6.2.14.2.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00272.md) | 361–361 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.14 SettlementParties &lt;SttlmPties&gt; / 11.4.6.2.14.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.6.2.14.2.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00273.md) | 362–362 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.15 AdditionalSettlementObligationDetails &lt;AddtlSttlmOblgtnDtls&gt; / 11.4.6.2.15.1 RelatedSettlementObligationIdentification &lt;RltdSttlmOblgtnId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00274.md) | 363–363 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.15 AdditionalSettlementObligationDetails &lt;AddtlSttlmOblgtnDtls&gt; / 11.4.6.2.15.2 ObligationType &lt;OblgtnTp&gt; / 11.4.6.2.15.2.1 Code &lt;Cd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00275.md) | 364–364 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.15 AdditionalSettlementObligationDetails &lt;AddtlSttlmOblgtnDtls&gt; / 11.4.6.2.15.6 NetPositionPrice &lt;NetPosPric&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00276.md) | 365–365 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.15 AdditionalSettlementObligationDetails &lt;AddtlSttlmOblgtnDtls&gt; / 11.4.6.2.15.9 SettlementDate &lt;SttlmDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00277.md) | 366–366 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.6 ReportDetails &lt;RptDtls&gt; / 11.4.6.2 SettlementObligationDetails &lt;SttlmOblgtnDtls&gt; / 11.4.6.2.15 AdditionalSettlementObligationDetails &lt;AddtlSttlmOblgtnDtls&gt; / 11.4.6.2.15.12 References &lt;Refs&gt; / 11.4.6.2.15.12.1 TradeLegNotificationIdentification &lt;TradLegNtfctnId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00278.md) | 367–367 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.7 SettlementParties &lt;SttlmPties&gt; / 11.4.7.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00279.md) | 368–368 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.7 SettlementParties &lt;SttlmPties&gt; / 11.4.7.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.7.1.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00280.md) | 369–369 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.7 SettlementParties &lt;SttlmPties&gt; / 11.4.7.1 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt; / 11.4.7.1.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00281.md) | 370–370 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.7 SettlementParties &lt;SttlmPties&gt; / 11.4.7.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.7.2.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00282.md) | 371–371 |
| [11 MX secl.010.001.04 SettlementObligationReportV04 / 11.4 Message Building Blocks / 11.4.7 SettlementParties &lt;SttlmPties&gt; / 11.4.7.2 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 11.4.7.2.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00283.md) | 372–372 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Broker](../../../../../shared/reference/participants/participant-src-000052-broker.md) | participant | src-000052 |
| [CCP](../../../../../shared/reference/participants/participant-src-000052-ccp.md) | participant | src-000052 |
| [Central Counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | participant | src-000052 |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | participant | src-000052 |
| [Central Securities Depository (CSD)](../../../../../shared/reference/participants/participant-src-000052-central-securities-depository-csd.md) | participant | src-000052 |
| [Clearing Member (CM)](../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | participant | src-000052 |
| [Clearing Member (G or I)](../../../../../shared/reference/participants/participant-src-000052-clearing-member-g-or-i.md) | participant | src-000052 |
| [Global Custodian](../../../../../shared/reference/participants/participant-src-000052-global-custodian.md) | participant | src-000052 |
| [(Individual or General) Clearing Member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | participant | src-000052 |
| [Sub-Custodian](../../../../../shared/reference/participants/participant-src-000052-sub-custodian.md) | participant | src-000052 |
| [BusinessProcess - Trade Management](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md) | business-flow | src-000052 |
| [BusinessProcess - Risk Management – Netting Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p194-business-process-risk-management-netting-process.md) | business-flow | src-000052 |
| [BusinessProcess - Risk Management – Margining Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p196-business-process-risk-management-margining-process.md) | business-flow | src-000052 |
| [BusinessProcess - Risk Management – Default Fund Contribution Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process.md) | business-flow | src-000052 |
| [BusinessProcess - Settlement Management – Settlement Netting Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md) | business-flow | src-000052 |
| [Settlement Management – Buy-In Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md) | business-flow | src-000052 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
