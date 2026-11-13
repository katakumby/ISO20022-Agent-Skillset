---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.7 SettlementInformation <SttlmInf>", "5.4.3.21.7.7 InstructedReimbursementAgentAccount <InstdRmbrsmntAgtAcct>"]
file_pages: [627]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.7.7 InstructedReimbursementAgentAccount <InstdRmbrsmntAgtAcct>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 627 to 627.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 627

```text
InstructedReimbursementAgent <InstdRmbrsmntAgt> contains the following elements (see
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
5.4.3.21.7.7  InstructedReimbursementAgentAccount <InstdRmbrsmntAgtAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the instructed reimbursement agent account at
its servicing agent in the payment chain.
Impacted by: C20 "IdentificationOrProxyPresenceRule", C19 "IdentificationAndProxyGuideline"
InstructedReimbursementAgentAccount <InstdRmbrsmntAgtAcct> contains the following
elements (see "CashAccount40" on page 1161 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1161
   Type <Tp> [0..1] ± 1161
   Currency <Ccy> [0..1] CodeSet C2 1162
   Name <Nm> [0..1] Text 1162
   Proxy <Prxy> [0..1] ± 1162
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
627 March 2026
```

