---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.52 SecurityCSDLink <SctyCSDLk>", "32.4.3.1.1.3.52.7 IssuanceAccount <IssncAcct>", "32.4.3.1.1.3.52.7.2 PrimaryAccountIndicator <PmryAcctInd>"]
file_pages: [2034]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.52.7.2 PrimaryAccountIndicator <PmryAcctInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2034 to 2034.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2034

```text
IssuanceAccount <IssncAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
32.4.3.1.1.3.52.7.2  PrimaryAccountIndicator <PmryAcctInd>
Presence: [1..1]
Definition: Defines if the related issuance account is the primary account or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
32.4.3.1.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Provides the business error details.
BusinessError <BizErr> contains the following BusinessError4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
2034
   BusinessError <BizErr> [1..*]  2035
     Error <Err> [1..1]  2036
{Or       Code <Cd> [1..1] CodeSet 2036
Or}       Proprietary <Prtry> [1..1] Text 2036
     Description <Desc> [0..1] Text 2036
32.4.3.1.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Way(s) of identifying the security.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C8 "ISINGuideline", C9
"ISINPresenceRule", C12 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2034 August 2026
```

