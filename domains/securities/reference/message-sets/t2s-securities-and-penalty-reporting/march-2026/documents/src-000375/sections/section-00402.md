---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.10 CorporateActionOption5Code"]
file_pages: [501]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.10 CorporateActionOption5Code

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 501 to 501.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 501

```text
CodeName Name Definition
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
7.2.2.10  CorporateActionOption5Code
Definition: Specifies the corporate action options available to the account owner.
Type: CodeSet
CodeName Name Definition
CASH Cash Option to choose cash.
SECU Security Distribution of securities to holders.
7.2.2.11  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.2.2.12  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
7.2.2.13  DateType3Code
Definition: Specifies a type of date.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 501 March 2026
```

