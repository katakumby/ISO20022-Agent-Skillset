---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.9.5 DematerialisedIndicator <DmtrlsdInd>"]
file_pages: [676]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.9.5 DematerialisedIndicator <DmtrlsdInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 676 to 676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 676

```text
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
28.4.9.5  DematerialisedIndicator <DmtrlsdInd>
Presence: [0..1]
Definition: Indicates whether a security exists only as an electronic record, that is, there is no physical
document representing the security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
28.4.9.6  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference2Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
SECU Securities Distribution in securities.
28.4.9.7  BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn>
Presence: [0..1]
Definition: Beneficial owner or its designated agent certifies that it complies with any holding or
investment restrictions or requirements of the fund.
Datatype: "BeneficiaryCertificationCompletion1Code" on page 5277
CodeName Name Definition
NCER CertificationNotRequired Certification is not required for this fund.
ELEC ElectronicCertification Electronic certification is acceptable.
PHYS PhysicalCertification Electronic certification is not acceptable
and is required in physical form.
28.4.9.8  RequestedTradeDate <ReqdTradDt>
Presence: [0..1]
Definition: Date to be used as the trade date when securities are settled through an International
Central Securities Depository (ICSD) or Central Securities Depository (CSD).
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 676 May 2026
```

