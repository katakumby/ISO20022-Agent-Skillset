---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.22 StatementUpdateTypeCodeAndDSSCode1Choice"]
file_pages: [311]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.22 StatementUpdateTypeCodeAndDSSCode1Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 311 to 311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 311

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification7" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 276
   Information <Inf> [1..1] Text 276
7.1.19.22  StatementUpdateTypeCodeAndDSSCode1Choice
Definition: Choice between formats for the update type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementUpdateTypeAsCode <StmtUpdTpAsCd> [1..1] CodeSet 311
Or}   StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> [1..1] ± 311
7.1.19.22.1  StatementUpdateTypeAsCode <StmtUpdTpAsCd>
Presence: [1..1]
Definition: Update type expressed as a code.
Datatype: "StatementUpdateType1Code" on page 652
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
7.1.19.22.2  StatementUpdateTypeAsDSS <StmtUpdTpAsDSS>
Presence: [1..1]
Definition: Update type expressed as a data source scheme and a code used within the data source
scheme.
StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> contains the following elements (see
"GenericIdentification7" on page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 276
   Information <Inf> [1..1] Text 276
7.1.19.23  SecuritiesRTGS4Choice
Definition: Choice of format for the securities RTGS information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 312
Or}   Proprietary <Prtry> [1..1] ± 312
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 311 February 2025
```

