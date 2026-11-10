---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.13 Payment", "10.1.13.1 SettlementTimeRequest2", "10.1.13.1.2 TillTime <TillTm>"]
file_pages: [1203]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.13.1.2 TillTime <TillTm>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1203 to 1203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1203

```text
10.1.13.1.2  TillTime <TillTm>
Presence: [0..1]
Definition: Time until when the payment may be settled.
Datatype: "ISOTime" on page 1247
10.1.13.1.3  FromTime <FrTm>
Presence: [0..1]
Definition: Time as from when the payment may be settled.
Datatype: "ISOTime" on page 1247
10.1.13.1.4  RejectTime <RjctTm>
Presence: [0..1]
Definition: Time by when the payment must be settled to avoid rejection.
Datatype: "ISOTime" on page 1247
10.1.13.2  InstructionForCreditorAgent3
Definition: Further information related to the processing of the payment instruction that may need to be
acted upon by the creditor's agent. The instruction may relate to a level of service, or may be an
instruction that has to be executed by the creditor's agent, or may be information required by the
creditor's agent.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 1203
   InstructionInformation <InstrInf> [0..1] Text 1203
10.1.13.2.1  Code <Cd>
Presence: [0..1]
Definition: Coded information related to the processing of the payment instruction, provided by the
initiating party, and intended for the creditor's agent.
Datatype: "ExternalCreditorAgentInstruction1Code" on page 1228
10.1.13.2.2  InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Further information complementing the coded instruction or instruction to the creditor's agent
that is bilaterally agreed or specific to a user community.
Datatype: "Max140Text" on page 1244
10.1.14 Payment Type
10.1.14.1  PaymentTypeInformation28
Definition: Provides further details of the type of payment.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1203 March 2026
```

