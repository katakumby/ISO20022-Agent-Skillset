---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.4 Message Building Blocks", "6.4.5 ReportDetails <RptDtls>", "6.4.5.1 MarginProduct <MrgnPdct>", "6.4.5.1.1 Code <Cd>"]
file_pages: [241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.4.5.1.1 Code <Cd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 241 to 241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 241

```text
6.4.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the underlying product of the margin using a code.
Datatype: MarginProduct1Code on page 478
CodeName Name Definition
EQUI Equities Specifies that the margin is related to
equities.
FIXI FixedIncome Specifies that the margin is related to
fixed income.
6.4.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the underlying product of the margin using a proprietary format.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
6.4.5.2  MarginAccount <MrgnAcct>
Presence: [1..1]
Definition: Identifies the clearing member's account.
MarginAccount <MrgnAcct> contains the following elements (see SecuritiesAccount18 on page 373
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 373
   Type <Tp> [1..1] CodeSet 373
   Name <Nm> [0..1] Text 373
6.4.5.3  CollateralisedMarginAccountIndicator <CollsdMrgnAcctInd>
Presence: [0..1]
Definition: Used to indicate whether the reported margin account is collateralised or not. If not
collateralised, the account is configured for informational reporting.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 241
```

