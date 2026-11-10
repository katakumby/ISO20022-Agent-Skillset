---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
flow_id: "bah-signing-business-message"
source_locations: ["§4.1 p28; §§4.2.6–4.2.12 pp31–33; Figure 4 p34"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-authorised-signatory", "bah-signature-verifier", "bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["Historical illustrative signature profile; exact V04 applicability not assumed.", "Figure 4 connector discrepancy issue-000017."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Construct the BAH signature as the final creation step

## Purpose, trigger and preconditions

An application has a Business Message to sign under agreed implementation guidelines. BAH and ISO message content are ready after any business approval/amendment. Signature creator and verifiers agree the signature structure and contextual constraints; signing authority is determined outside the annex. [§4.1 p28; §§4.2.6–4.2.12 pp31–33; Figure 4 p34](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Participants

- [bah-authorised-signatory](../../../../participants/bah-authorised-signatory.md).
- [bah-signature-verifier](../../../../participants/bah-signature-verifier.md).
- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

Signing implementation is an implementation of the signatory’s technical process, not a newly asserted institution. The source does not say the authorised person must be the messaging endpoint.

## Activities and decisions

| Step | Responsible participant | Activity / decision | Message or context |
| --- | --- | --- | --- |
| 1 | Authorised signatory / signing implementation | Obtain the Business Message and construct KeyInfo with certificate and unique Id. | Local construction; no new business-message exchange specified. |
| 2 | Signing implementation | Extract BAH, remove enveloped Signature, canonicalize and calculate its digest. | BAH context. |
| 3 | Signing implementation | Extract the ISO 20022 Message, canonicalize and calculate its digest. | ISO message context. |
| 4 | Signing implementation | Canonicalize KeyInfo and calculate its digest. | KeyInfo context. |
| 5 | Signing implementation | Place the three digests in References using text-defined URI rules: BAH empty URI, ISO message URI absent, KeyInfo #Id. | Figure 4 connector discrepancy remains issue-000017. |
| 6 | Authorised signatory / signing implementation | Canonicalize SignedInfo, perform the signing algorithm, insert SignatureValue as final creation step. | Private-key signing in the introductory figure. |
| 7 | Sending messaging endpoint | Send the resulting signed Business Message to the receiving endpoint. | Sending endpoint → receiving endpoint; generic transport shown in Figure 2. |

All steps: [§4.1 p28; §§4.2.6–4.2.12 pp31–33; Figure 4 p34](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Alternatives and failures

Figure 4’s apparent connector mapping is not silently corrected. Text-defined URI rules and drawn connectors are recorded separately. The source supplies no business cancellation/reversal or signer-authorisation failure workflow. [§4.1 p28; §§4.2.6–4.2.12 pp31–33; Figure 4 p34](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Outcomes and postconditions

SignatureValue has been inserted into the completed Business Message; receipt or successful verification is a separate flow. [§4.1 p28; §§4.2.6–4.2.12 pp31–33; Figure 4 p34](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).

## Diagrams and relationships

- [fig-0031](../documents/src-000012/pdf-figures/fig-0031.md).
- [fig-0032](../documents/src-000012/pdf-figures/fig-0032.md).
- [fig-0033](../documents/src-000012/pdf-figures/fig-0033.md).

[Signature structure, rule details and limitations](../../../../concepts/bah-signature-guidelines.md) · [Signed-message business usage](signed-message.md)
