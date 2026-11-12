---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.15 PaymentSignature <PmtSgntr>", "6.4.2.15.1 ILPV4 <ILPV4>"]
file_pages: [750]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.15.1 ILPV4 <ILPV4>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 750 to 750.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 750

```text
6.4.2.15.1  ILPV4 <ILPV4>
Presence: [1..1]
Definition: Cryptographic key represented as a ILP V4 packet.
Datatype: "HexBinaryText" on page 1243
6.4.2.15.2  Signature <Sgntr>
Presence: [1..1]
Definition: Cryptographic key represented as a signature.
Datatype: "SHA256SignatureText" on page 1247
6.4.2.16  PreviousInstructingAgent1 <PrvsInstgAgt1>
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
6.4.2.17  PreviousInstructingAgent1Account <PrvsInstgAgt1Acct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the previous instructing agent at its servicing
agent in the payment chain.
Impacted by: C17 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
750 March 2026
```

