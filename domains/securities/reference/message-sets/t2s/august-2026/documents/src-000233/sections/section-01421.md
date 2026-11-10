---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.52 SecurityCSDLink <SctyCSDLk>", "32.4.3.1.1.3.52.1 ValidFrom <VldFr>"]
file_pages: [2030]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.52.1 ValidFrom <VldFr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2030 to 2030.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2030

```text
SecurityCSDLink <SctyCSDLk> contains the following SecurityCSDLink7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] ± 2030
   ValidTo <VldTo> [0..1] ± 2030
   SecurityMaintenance <SctyMntnc> [0..1] Indicator 2031
   IssuerCSD <IssrCSD> [0..1]  2031
{Or     OrganisationIdentification <OrgId> [1..1] ± 2031
Or}     CombinedIdentification <CmbndId> [1..1] ± 2031
   InvestorCSD <InvstrCSD> [0..1]  2032
{Or     OrganisationIdentification <OrgId> [1..1] ± 2032
Or}     CombinedIdentification <CmbndId> [1..1] ± 2032
   TechnicalIssuerCSD <TechIssrCSD> [0..1]  2032
{Or     OrganisationIdentification <OrgId> [1..1] ± 2033
Or}     CombinedIdentification <CmbndId> [1..1] ± 2033
   IssuanceAccount <IssncAcct> [0..*]  2033
     IssuanceAccount <IssncAcct> [1..1] ± 2033
     PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2034
32.4.3.1.1.3.52.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the CSD is linked to the security.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
32.4.3.1.1.3.52.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Defines the date until when the CSD is linked to the security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2030 August 2026
```

