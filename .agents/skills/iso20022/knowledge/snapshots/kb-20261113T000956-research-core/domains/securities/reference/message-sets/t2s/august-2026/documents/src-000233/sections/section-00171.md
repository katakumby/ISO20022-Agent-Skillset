---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.4 Message Building Blocks", "13.4.5 CashAccount <CshAcct>"]
file_pages: [223]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.4.5 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 223 to 223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 223

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 3185 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 3185
Or   Rejected <Rjctd> [1..1] ± 3185
Or   Repair <Rpr> [1..1] ± 3186
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3186
Or   Proprietary <Prtry> [1..1] ± 3187
Or   Denied <Dnd> [1..1] ± 3187
Or}   Cancelled <Canc> [1..1] ± 3187
13.4.5 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which an entry is made.
Impacted by: C12 "IdentificationOrProxyPresenceRule", C11 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 2832 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2832
   Type <Tp> [0..1] ± 2832
   Currency <Ccy> [0..1] CodeSet C1 2833
   Name <Nm> [0..1] Text 2833
   Proxy <Prxy> [0..1] ± 2833
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
13.4.6 CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 223 August 2026
```

