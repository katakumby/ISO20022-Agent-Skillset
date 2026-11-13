---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.1 GroupHeader <GrpHdr>", "7.4.1.6 ControlSum <CtrlSum>"]
file_pages: [851, 852]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.1.6 ControlSum <CtrlSum>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 851 to 852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 851

```text
7.4.1.6  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
7.4.1.7  TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt>
Presence: [0..1]
Definition: Total amount of money moved between the instructing agent and the instructed agent.
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
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
7.4.1.8  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
7.4.1.9  SettlementInformation <SttlmInf>
Presence: [1..1]
Definition: Specifies the details on how the settlement of the transaction(s) between the instructing
agent and the instructed agent is completed.
Impacted by: C18 "InstructedReimbursementAgentAccountRule", C20
"InstructingReimbursementAgentAccountRule", C59 "SettlementMethodAgentRule", C60
"SettlementMethodClearingRule", C61 "SettlementMethodCoverAgentRule", C62
"SettlementMethodCoverRule", C65 "ThirdReimbursementAgentAccountRule", C66
"ThirdReimbursementAgentRule"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
851 March 2026
```

## File page 852

```text
SettlementInformation <SttlmInf> contains the following SettlementInstruction15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementMethod <SttlmMtd> [1..1] CodeSet 853
   SettlementAccount <SttlmAcct> [0..1] ± C16,
C15
854
   ClearingSystem <ClrSys> [0..1]  854
{Or     Code <Cd> [1..1] CodeSet 855
Or}     Proprietary <Prtry> [1..1] Text 855
   InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 855
   InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
856
   InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 856
   InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
857
   ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 858
   ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
858
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
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
852 March 2026
```

