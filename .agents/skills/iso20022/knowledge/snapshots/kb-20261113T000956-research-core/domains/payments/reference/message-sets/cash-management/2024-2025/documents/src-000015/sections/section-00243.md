---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.4 Message Building Blocks", "7.4.4 CancellationReason <CxlRsn>"]
file_pages: [361]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7.4.4 CancellationReason <CxlRsn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 361 to 361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 361

```text
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
7.4.4 CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Provides detailed information on the cancellation reason.
CancellationReason <CxlRsn> contains the following PaymentCancellationReason6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 361
   Reason <Rsn> [0..1] ± 362
   AdditionalInformation <AddtlInf> [0..*] Text 363
7.4.4.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the cancellation request.
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 361 February 2025
```

