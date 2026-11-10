---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.2 CodeSet", "10.2.2.5 EligibilityType1Code"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.2.5 EligibilityType1Code

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
10.2.2.5  EligibilityType1Code
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
10.2.2.6  ExternalCollateralReferenceDataStatusReason1Code
Definition: Specifies the status reason, as published in an external collateral reference data status
reason code list.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
10.2.2.7  ExternalFinancialInstrumentIdentificationType1Code
Definition: Specifies the external financial instrument identification type scheme name code in the
format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 79 May 2025
```

