---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "4.4.3.27.24.9 PaymentSignature <PmtSgntr>", "4.4.3.27.24.9.2 Signature <Sgntr>"]
file_pages: [538]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24.9.2 Signature <Sgntr>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 538 to 538.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 538

```text
Definition: Cryptographic key represented as a ILP V4 packet.
Datatype: "HexBinaryText" on page 1243
4.4.3.27.24.9.2  Signature <Sgntr>
Presence: [1..1]
Definition: Cryptographic key represented as a signature.
Datatype: "SHA256SignatureText" on page 1247
4.4.3.27.24.10  PreviousInstructingAgent1 <PrvsInstgAgt1>
Presence: [0..1]
Definition: Agent between the debtor's agent and the instructing agent.
Usage: If more than one previous instructing agent is present, then PreviousInstructingAgent1 identifies
the agent between the DebtorAgent and the PreviousInstructingAgent2.
PreviousInstructingAgent1 <PrvsInstgAgt1> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
4.4.3.27.24.11  PreviousInstructingAgent1Account <PrvsInstgAgt1Acct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the previous instructing agent at its servicing
agent in the payment chain.
Impacted by: C22 "IdentificationOrProxyPresenceRule", C21 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
538 March 2026
```

