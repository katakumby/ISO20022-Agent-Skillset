---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.7 SettlementInformation <SttlmInf>", "2.4.3.18.7.5 InstructingReimbursementAgentAccount <InstgRmbrsmntAgtAcct>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.7.5 InstructingReimbursementAgentAccount <InstgRmbrsmntAgtAcct>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
2.4.3.18.7.5  InstructingReimbursementAgentAccount <InstgRmbrsmntAgtAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the instructing reimbursement agent account at
its servicing agent in the payment chain.
Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"
InstructingReimbursementAgentAccount <InstgRmbrsmntAgtAcct> contains the following
elements (see "CashAccount40" on page 1161 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1161
   Type <Tp> [0..1] ± 1161
   Currency <Ccy> [0..1] CodeSet C2 1162
   Name <Nm> [0..1] Text 1162
   Proxy <Prxy> [0..1] ± 1162
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
2.4.3.18.7.6  InstructedReimbursementAgent <InstdRmbrsmntAgt>
Presence: [0..1]
Definition: Agent at which the instructed agent will be reimbursed.
Usage: If InstructedReimbursementAgent contains a branch of the InstructedAgent, then the party in
InstructedAgent will claim reimbursement from that branch/will be paid by that branch.
Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only
InstructingReimbursementAgent must be used.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
56 March 2026
```

