---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.3 RequestedAdviceType <ReqdAdvcTp>", "5.4.2.3.1 CreditAdvice <CdtAdvc>"]
file_pages: [427]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.3.1 CreditAdvice <CdtAdvc>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 427 to 427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
RequestedAdviceType <ReqdAdvcTp> contains the following AdviceType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditAdvice <CdtAdvc> [0..1]  427
{Or     Code <Cd> [1..1] CodeSet 427
Or}     Proprietary <Prtry> [1..1] Text 427
   DebitAdvice <DbtAdvc> [0..1]  427
{Or     Code <Cd> [1..1] CodeSet 428
Or}     Proprietary <Prtry> [1..1] Text 428
5.4.2.3.1  CreditAdvice <CdtAdvc>
Presence: [0..1]
Definition: Type of credit advice requested.
CreditAdvice <CdtAdvc> contains one of the following AdviceType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 427
Or}   Proprietary <Prtry> [1..1] Text 427
5.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Advice type, in a coded form.
Datatype: "AdviceType1Code" on page 587
CodeName Name Definition
ADWD AdviceWithDetails Advice with transaction details is
requested.
ADND AdviceWithoutDetails Advice without transaction details is
requested.
5.4.2.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Advice type, in a proprietary form.
Datatype: "Max35Text" on page 609
5.4.2.3.2  DebitAdvice <DbtAdvc>
Presence: [0..1]
Definition: Type de debit advice requested.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 427 March 2026
```

