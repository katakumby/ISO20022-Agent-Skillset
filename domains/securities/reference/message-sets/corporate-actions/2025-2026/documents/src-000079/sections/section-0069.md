---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"]
content_origin: "source-transcription"
---

# Scenario 5: Mandatory Event with Reversal of Payment

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 5: Mandatory Event with Reversal of Payment.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P340** Scenario 5: Mandatory Event with Reversal of Payment

**P341** The account servicer announces a mandatory event. A CA Movement Preliminary Advice is sent prior to payment date. Following confirmation of the payment, a reversal needs to be made for which a CA Movement Preliminary Advice of reversal is made prior to the effective reversal of payment.

[fig-0037 - original figure evidence](../diagrams/fig-0037.md)

**P343** CAFE and CACO Movements usage guidelines

**P344** Movements reported within the CA movement preliminary advice reversal (CAFE reversal) message will be opposite to those reported into the referred CA confirmation message (CACO) i.e. credit of cash and/or securities will become debits and inversely.

**P345** Movements reported within the CA Reversal (CARE) message will be identical to the movements reported into the referred CA confirmation message (CACO).

**P346** If a rebook follows a reversal, it is recommended that the rebook be considered a new payment. Therefore, subject to the pre-advice process if it meets the criteria agreed upon between the account servicer and the account provider.

