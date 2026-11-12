---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.21 UltimateCreditor <UltmtCdtr>"]
file_pages: [698]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.21 UltimateCreditor <UltmtCdtr>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 698 to 698.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 698

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
5.4.3.21.21  UltimateCreditor <UltmtCdtr>
Presence: [0..1]
Definition: Ultimate party to which an amount of money is due.
UltimateCreditor <UltmtCdtr> contains one of the following Party50Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Party <Pty> [1..1] ± 698
Or}   Agent <Agt> [1..1] ± 699
5.4.3.21.21.1  Party <Pty>
Presence: [1..1]
Definition: Identification of a person or an organisation.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
698 March 2026
```

