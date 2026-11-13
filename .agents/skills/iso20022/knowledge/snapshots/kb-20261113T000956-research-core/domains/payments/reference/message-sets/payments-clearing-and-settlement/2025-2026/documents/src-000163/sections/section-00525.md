---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.1.6 ControlSum <CtrlSum>"]
file_pages: [719, 720]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.1.6 ControlSum <CtrlSum>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 719 to 720.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 719

```text
6.4.1.6  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
6.4.1.7  TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt>
Presence: [0..1]
Definition: Total amount of money moved between the instructing agent and the instructed agent.
Impacted by: C1 "ActiveCurrency", C11 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1222
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.4.1.8  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
6.4.1.9  SettlementInformation <SttlmInf>
Presence: [1..1]
Definition: Specifies the details on how the settlement of the transaction(s) between the instructing
agent and the instructed agent is completed.
Impacted by: C22 "InstructedReimbursementAgentAccountRule", C24
"InstructingReimbursementAgentAccountRule", C41 "SettlementMethodAgentRule", C42
"SettlementMethodClearingRule", C43 "SettlementMethodCoverAgentRule", C44
"SettlementMethodCoverRule", C47 "ThirdReimbursementAgentAccountRule", C48
"ThirdReimbursementAgentRule"
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
719 March 2026
```

## File page 720

```text
SettlementInformation <SttlmInf> contains the following SettlementInstruction15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementMethod <SttlmMtd> [1..1] CodeSet 721
   SettlementAccount <SttlmAcct> [0..1] ± C17,
C16
722
   ClearingSystem <ClrSys> [0..1]  722
{Or     Code <Cd> [1..1] CodeSet 723
Or}     Proprietary <Prtry> [1..1] Text 723
   InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 723
   InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C17,
C16
724
   InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 724
   InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C17,
C16
725
   ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 726
   ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C17,
C16
726
Constraints
• InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent must be
present.
On Condition
    /InstructedReimbursementAgent is absent
Following Must be True
    /InstructedReimbursementAgentAccount Must be absent
• InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent must be
present.
On Condition
    /InstructingReimbursementAgent is absent
Following Must be True
    /InstructingReimbursementAgentAccount Must be absent
• SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and ClearingSystem
are not allowed.
On Condition
    /SettlementMethod is equal to value 'InstructingAgent'
 Or    /SettlementMethod is equal to value 'InstructedAgent'
Following Must be True
    /ClearingSystem Must be absent
 And    /InstructingReimbursementAgent Must be absent
 And    /InstructedReimbursementAgent Must be absent
 And    /ThirdReimbursementAgent Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
720 March 2026
```

