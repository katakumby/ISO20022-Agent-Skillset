---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02", "18.4 Message Building Blocks", "18.4.1 MarketIdentification <MktId>", "18.4.1.4 Category <Ctgy>"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.049.001.02"]
---

# 18.4.1.4 Category <Ctgy>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
Datatype: "MarketIdentification1Code" on page 438
CodeName Name Definition
SGMT Segment Market segment code.
OPRT Operating Market operating code.
18.4.1.4  Category <Ctgy>
Presence: [0..1]
Definition: Provides the category of market the venue operates in.
Datatype: "MICEntityType1Code" on page 438
CodeName Name Definition
APPA ApprovedPublicationArrangement Person authorised under the provisions
established in the regulation to provide
the service of publishing trade reports on
behalf of investment firms.
CTPS ConsolidatedTapeProvider Provider which will consolidate post-
trade information into a continuous
electronic data stream and make it
publicly available as close to real time as
technologically possible on a reasonable
commercial basis and free of charge
after 15 minutes.
MLTF MultilateralTradingFacility Multilateral system which brings together
multiple third-party buying and selling
interests in financial instruments in a way
that results in a contract.
OTFS OrganisedTradingFacility Multilateral system which is not a
regulated market or multilateral trading
facility in which multiple third-party
buying and selling interests in bonds,
structured finance products, emission
allowances or derivatives are able to
interact in a way that results in a
contract.
RMKT RegulatedMarket Market on which financial instruments
can be traded according to rules defined
by the stock exchange.
SINT SystematicInternaliser Investment firm which, on an organised,
frequent systematic and substantial
basis, deals on own account when
executing client orders outside a
regulated market, an multilateral trading
facility or an organised trading facility
without operating a multilateral system.
18.4.1.5  InstitutionName <InstnNm>
Presence: [1..1]
Definition: The name or description of the institution, market, or infrastructure.
Datatype: "Max450Text" on page 456
Approved by the Securities SEG on 17 July 2025 auth.049.001.02
FinancialInstrumentReportingMarketIdentificationCo
deReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
255 July 2025
```

