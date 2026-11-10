---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.2 Message Datatypes"]
file_pages: [94]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.2 Message Datatypes

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 94 to 94.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 94

```text
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 94
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
11.2 Message Datatypes
11.2.1 CodeSet
11.2.1.1  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
11.2.1.2  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
11.2.1.3  DataModification1Code
Definition: Specified the type of modification to be applied on a data set.
Type: CodeSet
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 94 December 2019
```

