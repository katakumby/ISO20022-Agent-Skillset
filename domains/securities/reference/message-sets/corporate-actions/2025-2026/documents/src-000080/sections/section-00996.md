---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.135 SafekeepingPlace3Code"]
file_pages: [1242]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.135 SafekeepingPlace3Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1242 to 1242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1242

```text
16.2.2.135  SafekeepingPlace3Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
16.2.2.136  ShortLong1Code
Definition: Specifies whether the securities position is short or long, that is, whether the balance is a
negative or positive balance.
Type: CodeSet
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
16.2.2.137  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
16.2.2.138  TypeOfIdentification1Code
Definition: Specifies the type of alternate identification which can be used to give an alternate
identification of the party identified.
Type: CodeSet
CodeName Name Definition
ARNU AlienRegistrationNumber Number assigned by a government
agency to identify foreign nationals.
CCPT PassportNumber Number assigned by a passport
authority.
CHTY TaxExemptIdentificationNumber Number assigned to a tax exempt entity.
CORP CorporateIdentification Number assigned to a corporate entity.
DRLC DriverLicenseNumber Number assigned to a driver's license.
FIIN ForeignInvestmentIdentityNumber Number assigned to a foreign investor
(other than the alien number).
TXID TaxIdentificationNumber Number assigned by a tax authority to
an entity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1242 February 2026
```

