---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.8.5 DematerialisedIndicator <DmtrlsdInd>"]
file_pages: [588]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.8.5 DematerialisedIndicator <DmtrlsdInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 588 to 588.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 588

```text
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
26.4.8.5  DematerialisedIndicator <DmtrlsdInd>
Presence: [0..1]
Definition: Indicates whether a security exists only as an electronic record, that is, there is no physical
document representing the security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
26.4.8.6  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference2Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
SECU Securities Distribution in securities.
26.4.8.7  BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn>
Presence: [0..1]
Definition: Beneficial owner or its designated agent certifies that it complies with any holding or
investment restrictions or requirements of the fund.
Datatype: "BeneficiaryCertificationCompletion1Code" on page 5277
CodeName Name Definition
NCER CertificationNotRequired Certification is not required for this fund.
ELEC ElectronicCertification Electronic certification is acceptable.
PHYS PhysicalCertification Electronic certification is not acceptable
and is required in physical form.
26.4.8.8  RequestedTradeDate <ReqdTradDt>
Presence: [0..1]
Definition: Date used as the trade date when securities are settled through an International Central
Securities Depository (ICSD) or Central Securities Depository (CSD).
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 588 May 2026
```

