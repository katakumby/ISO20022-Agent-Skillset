---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.1 FinancialInstrument96", "66.1.18.1.2 DematerialisedBearerSecurities <DmtrlsdBrScties>"]
file_pages: [4486]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.1.2 DematerialisedBearerSecurities <DmtrlsdBrScties>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4486 to 4486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4486

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.2  DematerialisedBearerSecurities <DmtrlsdBrScties>
Presence: [0..1]
Definition: Indicates whether it is possible to hold bearer units/shares in paperless form.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.3  PhysicalRegisteredSecurities <PhysRegdScties>
Presence: [0..1]
Definition: Indicates whether it is possible to hold registered units/shares in this class in paperless form.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.4  DematerialisedRegisteredSecurities <DmtrlsdRegdScties>
Presence: [0..1]
Definition: Indicates whether it is possible to hold registered units/shares in this class in paperless form.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.1.5  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to the class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 5294
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
66.1.18.1.6  DividendPolicy <DvddPlcy>
Presence: [0..1]
Definition: Dividend policy of the fund, for example, cash, units.
Datatype: "DividendPolicy1Code" on page 5294
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4486 May 2026
```

