---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.10 InvestmentAccount76"]
file_pages: [4633]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.10 InvestmentAccount76

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4633 to 4633.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4633

```text
FiscalYear <FsclYr> contains one of the following elements (see "FiscalYear1Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StartDate <StartDt> [1..1] Date 4467
Or}   EndDate <EndDt> [1..1] Date 4468
66.1.24.10  InvestmentAccount76
Definition: Information about a securities account and its characteristics.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4634
   Designation <Dsgnt> [0..1] Text 4634
   FundType <FndTp> [0..1] Text 4634
   FundFamilyName <FndFmlyNm> [0..1] Text 4634
   SecurityDetails <SctyDtls> [0..1]  C15 4634
     Identification <Id> [1..1] ± 4635
     Name <Nm> [0..1] Text 4636
     ShortName <ShrtNm> [0..1] Text 4636
     SupplementaryIdentification <SplmtryId> [0..1] Text 4636
     ClassType <ClssTp> [0..1] Text 4637
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4637
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4637
     ProductGroup <PdctGrp> [0..1] Text 4637
   AccountOwner <AcctOwnr> [0..1]  4637
{Or     IndividualOwnerIdentification <IndvOwnrId> [1..1]  4638
{Or       IdentificationNumber <IdNb> [1..1] ± 4638
Or}       PersonName <PrsnNm> [1..1] ± 4638
Or}     OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± C21 4639
   Intermediary <Intrmy> [0..*] ± 4639
   AccountServicer <AcctSvcr> [0..1] ± 4640
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4633 May 2026
```

