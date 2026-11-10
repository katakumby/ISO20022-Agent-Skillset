---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.175 TypeOfIdentification1Code"]
file_pages: [3313]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.175 TypeOfIdentification1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3313 to 3313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3313

```text
82.2.2.175  TypeOfIdentification1Code
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
82.2.2.176  TypeOfPrice11Code
Definition: Specifies the type of price and information about the price.
Type: CodeSet
CodeName Name Definition
BIDE Bid Price is the calculated bid price of a
dual-priced fund (offer-bid prices), that
is, the selling price of the units for the
investor.
OFFR Offer Price is the calculated offer price of a
dual-priced investment fund (offer-bid
prices), that is, the buying price of the
units for an investor.
NAVL NetAssetValue Price is the net asset value per unit that
is used either as a transacting price for a
single-priced investment fund class, or
as a notional price for the calculation of
other prices.
CREA Creation Price is the calculated creation price of a
dual-priced investment fund (creation-
cancellation prices) and the highest
possible buying price of the units before
the initial charge. The actual buying or
offer price, which includes charges, will
be higher.
CANC Cancellation Price is the calculated cancellation price
of a dual-priced investment fund
(creation-cancellation price), and the
lowest possible valuation of the units on
any one-day. The actual selling or bid
price is usually higher.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3313 August 2026
```

