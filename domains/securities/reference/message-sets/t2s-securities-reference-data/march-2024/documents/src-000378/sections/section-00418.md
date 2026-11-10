---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.9 CallType1Code"]
file_pages: [513]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.9 CallType1Code

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 513 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 513

```text
CodeName Name Definition
TRYL True The yield calculated with coupon dates
moved from a weekend or holiday to the
next valid settlement date.
WRST ToWorstConvention The lowest yield to all possible
redemption date scenarios.
13.2.2.9  CallType1Code
Definition: Defines the type of execution of the call feature.
Type: CodeSet
CodeName Name Definition
LOTT Lottery Type of execution of the call feature is a
lottery.
PRTA ProRata Type of execution of the call feature is
pro-rata.
13.2.2.10  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.2.2.11  DistributionPolicy1Code
Definition: Specifies if income is to be paid out (distributed) or retained (accumulated).
Type: CodeSet
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
13.2.2.12  ExternalFinancialInstrumentIdentificationType1Code
Definition: Specifies the external financial instrument identification type scheme name code in the
format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 513 March 2024
```

