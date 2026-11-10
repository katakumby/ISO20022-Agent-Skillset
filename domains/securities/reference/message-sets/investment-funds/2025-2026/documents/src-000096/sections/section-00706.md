---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.8 PrimaryCorporateInvestor <PmryCorpInvstr>"]
file_pages: [964]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.8 PrimaryCorporateInvestor <PmryCorpInvstr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 964 to 964.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 964

```text
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
35.4.8 PrimaryCorporateInvestor <PmryCorpInvstr>
Presence: [0..1]
Definition: Information identifying the primary corporate investor, for example, name and address.
PrimaryCorporateInvestor <PmryCorpInvstr> contains the following elements (see "Organisation36"
on page 4904 for details)
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
35.4.9 SecondaryCorporateInvestor <ScndryCorpInvstr>
Presence: [0..1]
Definition: Information identifying the secondary corporate investor, for example, name and address.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 964 May 2026
```

