---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.6 ThirdPartyRights2", "66.1.24.6.4 LegalEntityIdentifier <LglNttyIdr>"]
file_pages: [4597, 4598]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.6.4 LegalEntityIdentifier <LglNttyIdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4597 to 4598.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4597

```text
66.1.24.6.4  LegalEntityIdentifier <LglNttyIdr>
Presence: [0..1]
Definition: Identification of the holder with a Legal Entity Identifier. This is a code allocated to a party as
described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)".
Datatype: "LEIIdentifier" on page 5395
66.1.24.6.5  Amount <Amt>
Presence: [0..1]
Definition: Amount of the third party right.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.24.6.6  Description <Desc>
Presence: [0..1]
Definition: Description of the third party right.
Datatype: "Max350Text" on page 5403
66.1.24.7  InvestmentAccountOwnershipInformation16
Definition: Characteristics of the ownership of a securities account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4597 May 2026
```

## File page 4598

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  4599
{Or     Organisation <Org> [1..1] ± C24 4599
Or}     IndividualPerson <IndvPrsn> [1..1] ± 4600
   MoneyLaunderingCheck <MnyLndrgChck> [0..1] ± 4602
   InvestorProfileValidation <InvstrPrflVldtn> [0..*]  4602
     CertificationIndicator <CertfctnInd> [0..1] Indicator 4603
     ValidatingParty <VldtngPty> [0..1] Text 4603
     CheckingParty <ChckngPty> [0..1] Text 4603
     ResponsibleParty <RspnsblPty> [0..1] Text 4604
     CertificateType <CertTp> [0..1] ± 4604
     CheckingDate <ChckngDt> [0..1] Date 4604
     CheckingFrequency <ChckngFrqcy> [0..1] CodeSet 4604
     NextRevisionDate <NxtRvsnDt> [0..1] Date 4605
     SalaryRange <SlryRg> [0..1] Text 4605
     SourceOfWealth <SrcOfWlth> [0..1] Text 4605
     CustomerConductClassification <CstmrCndctClssfctn> [0..1] ± 4605
     RiskLevel <RskLvl> [0..1] ± 4605
     KnowYourCustomerCheckType
<KnowYourCstmrChckTp>
[0..1] ± 4605
     KnowYourCustomerDatabaseCheck
<KnowYourCstmrDBChck>
[0..1] ± 4606
   OwnershipBeneficiaryRate <OwnrshBnfcryRate> [0..1] ± C25 4606
   ClientIdentification <ClntId> [0..1] Text 4606
   FiscalExemption <FsclXmptn> [0..1] Indicator 4607
   SignatoryRightIndicator <SgntryRghtInd> [0..1] Indicator 4607
   MiFIDClassification <MiFIDClssfctn> [0..1] ± 4607
   Notification <Ntfctn> [0..*] ± 4607
   FATCAFormType <FATCAFormTp> [0..*] ± 4607
   FATCAStatus <FATCASts> [0..*] ± 4608
   FATCAReportingDate <FATCARptgDt> [0..1] Date 4608
   CRSFormType <CRSFormTp> [0..*] ± 4608
   CRSStatus <CRSSts> [0..*] ± 4608
   CRSReportingDate <CRSRptgDt> [0..1] Date 4609
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4598 May 2026
```

