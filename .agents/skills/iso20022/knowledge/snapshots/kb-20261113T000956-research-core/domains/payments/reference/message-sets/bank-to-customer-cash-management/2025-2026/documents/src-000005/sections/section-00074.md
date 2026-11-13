---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.9 RelatedParties <RltdPties>", "2.4.2.15.18.2.9.4 UltimateDebtor <UltmtDbtr>"]
file_pages: [139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.9.4 UltimateDebtor <UltmtDbtr>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 139 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
2.4.2.15.18.2.9.4  UltimateDebtor <UltmtDbtr>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor.
UltimateDebtor <UltmtDbtr> contains one of the following Party50Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Party <Pty> [1..1] ± 139
Or}   Agent <Agt> [1..1] ± 140
2.4.2.15.18.2.9.4.1  Party <Pty>
Presence: [1..1]
Definition: Identification of a person or an organisation.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
139 March 2026
```

