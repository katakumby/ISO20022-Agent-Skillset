---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.9 RelatedParties <RltdPties>", "2.4.2.15.18.2.9.7 UltimateCreditor <UltmtCdtr>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.9.7 UltimateCreditor <UltmtCdtr>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

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
2.4.2.15.18.2.9.7  UltimateCreditor <UltmtCdtr>
Presence: [0..1]
Definition: Ultimate party to which an amount of money is due.
UltimateCreditor <UltmtCdtr> contains one of the following Party50Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Party <Pty> [1..1] ± 144
Or}   Agent <Agt> [1..1] ± 145
2.4.2.15.18.2.9.7.1  Party <Pty>
Presence: [1..1]
Definition: Identification of a person or an organisation.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
144 March 2026
```

