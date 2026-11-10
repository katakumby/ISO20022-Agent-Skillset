---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.11 OtherCorporateInvestor <OthrCorpInvstr>"]
file_pages: [1515]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.11 OtherCorporateInvestor <OthrCorpInvstr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1515 to 1515.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1515

```text
SecondaryCorporateInvestor <ScndryCorpInvstr> contains the following elements (see
"Organisation36" on page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
40.4.11 OtherCorporateInvestor <OthrCorpInvstr>
Presence: [0..*]
Definition: Information identifying the other corporate investors, for example, name and address.
OtherCorporateInvestor <OthrCorpInvstr> contains the following elements (see "Organisation36" on
page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
40.4.12 TransferorAccount <TrfrAcct>
Presence: [1..1]
Definition: Identification of the account owned by the investor at the old plan manager (account
servicer).
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1515 May 2026
```

