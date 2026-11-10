---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.1.9 SettlementInformation <SttlmInf>", "3.4.1.9.1 SettlementMethod <SttlmMtd>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.1.9.1 SettlementMethod <SttlmMtd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
SettlementInformation <SttlmInf> contains the following SettlementInstruction14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementMethod <SttlmMtd> [1..1] CodeSet 147
   SettlementAccount <SttlmAcct> [0..1] ± C15,
C14
147
   ClearingSystem <ClrSys> [0..1]  148
{Or     Code <Cd> [1..1] CodeSet 148
Or}     Proprietary <Prtry> [1..1] Text 148
Constraints
• SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ClearingSystem is not allowed.
On Condition
    /SettlementMethod is equal to value 'InstructingAgent'
 Or    /SettlementMethod is equal to value 'InstructedAgent'
Following Must be True
    /ClearingSystem Must be absent
• SettlementMethodClearingRule
If SettlementMethod is equal to CLRG, then ClearingSystem must be present and
SettlementAccount is not allowed.
On Condition
    /SettlementMethod is equal to value 'ClearingSystem'
Following Must be True
    /SettlementAccount Must be absent
 And    /ClearingSystem Must be present
3.4.1.9.1  SettlementMethod <SttlmMtd>
Presence: [1..1]
Definition: Method used to settle the (batch of) payment instructions.
Datatype: "SettlementMethod2Code" on page 1238
CodeName Name Definition
INDA InstructedAgent Settlement is done by the agent
instructed to execute a payment
instruction.
INGA InstructingAgent Settlement is done by the agent
instructing and forwarding the payment
to the next party in the payment chain.
CLRG ClearingSystem Settlement is done through a payment
clearing system.
3.4.1.9.2  SettlementAccount <SttlmAcct>
Presence: [0..1]
Definition: A specific purpose account used to post debit and credit entries as a result of the transaction.
Impacted by: C15 "IdentificationOrProxyPresenceRule", C14 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
147 March 2026
```

