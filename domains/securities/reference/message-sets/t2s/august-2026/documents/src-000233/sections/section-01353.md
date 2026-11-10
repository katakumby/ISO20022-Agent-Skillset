---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.1 SecurityStatus <SctySts>"]
file_pages: [1962]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.1 SecurityStatus <SctySts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1962 to 1962.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1962

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       CombinedIdentification <CmbndId> [1..1] ± 2032
     TechnicalIssuerCSD <TechIssrCSD> [0..1]  2032
{Or       OrganisationIdentification <OrgId> [1..1] ± 2033
Or}       CombinedIdentification <CmbndId> [1..1] ± 2033
     IssuanceAccount <IssncAcct> [0..*]  2033
       IssuanceAccount <IssncAcct> [1..1] ± 2033
       PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2034
32.4.3.1.1.3.1  SecurityStatus <SctySts>
Presence: [0..1]
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1962
Or}   Proprietary <Prtry> [1..1] ± 1962
32.4.3.1.1.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Datatype: "SecurityStatus2Code" on page 3300
CodeName Name Definition
ACTV Active The status is active.
INAC Inactive The status is inactive.
SUSP Suspended The status is suspended.
32.4.3.1.1.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Security status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1962 August 2026
```

