---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.3 InvestorProfileValidation <InvstrPrflVldtn>", "66.1.24.7.3.1 CertificationIndicator <CertfctnInd>"]
file_pages: [4603]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.3.1 CertificationIndicator <CertfctnInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4603 to 4603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4603

```text
InvestorProfileValidation <InvstrPrflVldtn> contains the following PartyProfileInformation5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
66.1.24.7.3.1  CertificationIndicator <CertfctnInd>
Presence: [0..1]
Definition: Indicates whether the certificate type has been obtained and verified.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.24.7.3.2  ValidatingParty <VldtngPty>
Presence: [0..1]
Definition: Identification of the person who validated the document.
Datatype: "Max140Text" on page 5402
66.1.24.7.3.3  CheckingParty <ChckngPty>
Presence: [0..1]
Definition: Identification of the person who checked the document.
Datatype: "Max140Text" on page 5402
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4603 May 2026
```

