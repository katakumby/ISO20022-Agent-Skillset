---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.37 EligibilityType1Code"]
file_pages: [3237]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.37 EligibilityType1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3237 to 3237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3237

```text
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
82.2.2.37  EligibilityType1Code
Definition: Defines the type of eligibility.
Type: CodeSet
CodeName Name Definition
SECU Securities Eligibility applies at securities level.
ISCS IssuerCSD Eligibility applies at the level of issuer
CSD.
All of the securities issued by the issuer
CSD are eligible.
CTRY Country Eligibility applies at country level.
All of the securities issued in that country
are eligible.
82.2.2.38  ErrorHandling1Code
Definition: Error codes generated when the response to a query exceeds the maximum size or the data
is not available.
Type: CodeSet
CodeName Name Definition
X020 DataNotYetAvailable Specifies the error code when the data
requested are not yet available.
X030 MessageSizeLimitExceeded Specifies the error code when the data
requested generates a message size
that exceed the processing capacity.
X050 DataNotAvailable Specifies the error code when the data
requested have not been found.
82.2.2.39  EventFrequency3Code
Definition: Specifies the regularity of an event.
Type: CodeSet
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QUTR Quarterly Event takes place every three months or
four times a year.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3237 August 2026
```

