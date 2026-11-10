---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.52 SecurityCSDLink <SctyCSDLk>", "13.1.6.3.52.1 ValidFrom <VldFr>"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.52.1 ValidFrom <VldFr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
SecurityCSDLink <SctyCSDLk> contains the following SecurityCSDLink7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] ± 399
   ValidTo <VldTo> [0..1] ± 399
   SecurityMaintenance <SctyMntnc> [0..1] Indicator 399
   IssuerCSD <IssrCSD> [0..1] ± 400
   InvestorCSD <InvstrCSD> [0..1] ± 400
   TechnicalIssuerCSD <TechIssrCSD> [0..1] ± 400
   IssuanceAccount <IssncAcct> [0..*]  400
     IssuanceAccount <IssncAcct> [1..1] ± 401
     PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 401
13.1.6.3.52.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the CSD is linked to the security.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 236 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 236
Or}   DateTime <DtTm> [1..1] DateTime 236
13.1.6.3.52.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Defines the date until when the CSD is linked to the security.
ValidTo <VldTo> contains one of the following elements (see "DateAndDateTime2Choice" on
page 236 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 236
Or}   DateTime <DtTm> [1..1] DateTime 236
13.1.6.3.52.3  SecurityMaintenance <SctyMntnc>
Presence: [0..1]
Definition: Specify if the involved CSD (issuer/technical issuer/investor) is also the maintainer of related
reference data.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 399 March 2024
```

