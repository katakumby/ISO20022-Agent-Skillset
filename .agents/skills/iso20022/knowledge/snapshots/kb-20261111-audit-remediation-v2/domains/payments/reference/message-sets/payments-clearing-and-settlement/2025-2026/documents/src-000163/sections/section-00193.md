---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.1.9 InterbankSettlementDate <IntrBkSttlmDt>"]
file_pages: [277, 278]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.1.9 InterbankSettlementDate <IntrBkSttlmDt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 277 to 278.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 277

```text
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
4.4.1.9  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
4.4.1.10  SettlementInformation <SttlmInf>
Presence: [1..1]
Definition: Specifies the details on how the settlement of the transaction(s) between the instructing
agent and the instructed agent is completed.
Impacted by: C24 "InstructedReimbursementAgentAccountRule", C26
"InstructingReimbursementAgentAccountRule", C63 "SettlementMethodAgentRule", C64
"SettlementMethodClearingRule", C65 "SettlementMethodCoverAgentRule", C66
"SettlementMethodCoverRule", C69 "ThirdReimbursementAgentAccountRule", C70
"ThirdReimbursementAgentRule"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
277 March 2026
```

## File page 278

```text
SettlementInformation <SttlmInf> contains the following SettlementInstruction15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementMethod <SttlmMtd> [1..1] CodeSet 279
   SettlementAccount <SttlmAcct> [0..1] ± C22,
C21
280
   ClearingSystem <ClrSys> [0..1]  280
{Or     Code <Cd> [1..1] CodeSet 281
Or}     Proprietary <Prtry> [1..1] Text 281
   InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 281
   InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C22,
C21
282
   InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 282
   InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C22,
C21
283
   ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 284
   ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C22,
C21
284
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
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
278 March 2026
```

