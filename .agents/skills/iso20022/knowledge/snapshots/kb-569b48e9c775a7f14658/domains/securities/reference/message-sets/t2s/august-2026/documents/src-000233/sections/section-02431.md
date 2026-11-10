---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.27 CorporateActionOption5Code"]
file_pages: [3234]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.27 CorporateActionOption5Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3234 to 3234.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3234

```text
CodeName Name Definition
accrues during an accounting period is
retained within the fund instead of being
paid away to investors. The retained
income is nonetheless deemed to have
been distributed to investors for tax
purposes.
MTNG SecuritiesHoldersMeeting Ordinary or annual or extraordinary or
special general meeting.
INFO Information Information provided by the issuer
having no accounting/financial impact on
the holder.
TNDP TaxOnNonDistributedProceeds Taxable component on non-distributed
proceeds, for example, Australian
deemed income or US 871m income
regulation.
82.2.2.27  CorporateActionOption5Code
Definition: Specifies the corporate action options available to the account owner.
Type: CodeSet
CodeName Name Definition
CASH Cash Option to choose cash.
SECU Security Distribution of securities to holders.
82.2.2.28  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.2.2.29  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3234 August 2026
```

