---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
flow_id: "bah-verifying-signature"
source_locations: ["§4.1–4.2 p28; Figure 2 p29; §4.2.2 p30; §§4.2.6–4.2.12 pp31–33; Figure 5 p35"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-authorised-signatory", "bah-signature-verifier", "bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["Historical illustrative signature profile; exact V04 applicability not assumed."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Verify a received BAH signature

## Purpose, trigger and preconditions

A participant receives a signed Business Message to verify under agreed signature rules. Creator and verifier agree the structure and contextual constraints. The two XML contexts and the certificate/public validation key must be available according to the guide’s profile. [§4.1–4.2 p28; Figure 2 p29; §4.2.2 p30; §§4.2.6–4.2.12 pp31–33; Figure 5 p35](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Participants

- [bah-authorised-signatory](../../../../participants/bah-authorised-signatory.md).
- [bah-signature-verifier](../../../../participants/bah-signature-verifier.md).
- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

Signing implementation is an implementation of the signatory’s technical process, not a newly asserted institution. The source does not say the authorised person must be the messaging endpoint.

## Activities and decisions

| Step | Responsible participant | Activity / decision | Message or context |
| --- | --- | --- | --- |
| 1 | Receiving endpoint / verifier | Make the received Business Message available. | Prior exchange: sending endpoint → receiving endpoint. |
| 2 | Signature verifier | Extract BAH, apply enveloped-signature transform and canonicalization, then calculate digest. | Compare against empty-URI Reference. |
| 3 | Signature verifier | Extract ISO message, canonicalize and calculate digest. | Compare against URI-absent Reference. |
| 4 | Signature verifier | Extract KeyInfo, canonicalize and calculate digest. | Compare against #KeyInfo-id Reference. |
| 5 | Signature verifier | Decision: do all Reference comparisons succeed? No → verification failed. Yes → continue. | Figure 5 p35. |
| 6 | Signature verifier | Obtain SignatureValue, SignedInfo and certificate; perform verification algorithm. | The explanatory text identifies canonicalized SignedInfo, certified public key and SignatureValue inputs. |
| 7 | Signature verifier | Decision: algorithm verification successful? No → verification failed; Yes → verification successful. | No external response message is specified by the figure. |

All steps: [§4.1–4.2 p28; Figure 2 p29; §4.2.2 p30; §§4.2.6–4.2.12 pp31–33; Figure 5 p35](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Alternatives and failures

The introductory generic Figure 2 checks the cryptographic signature before digest comparison. Detailed BAH Figure 5 checks References first. These source variants are preserved. Each negative branch is terminal verification failure; the source does not prescribe a business rejection/cancellation message here. [§4.1–4.2 p28; Figure 2 p29; §4.2.2 p30; §§4.2.6–4.2.12 pp31–33; Figure 5 p35](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Outcomes and postconditions

Both digest consistency and signature verification pass, or verification fails. Presence of Signature alone does not prove a successful outcome. [§4.1–4.2 p28; Figure 2 p29; §4.2.2 p30; §§4.2.6–4.2.12 pp31–33; Figure 5 p35](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Diagrams and relationships

- [fig-0031](../documents/src-000012/pdf-figures/fig-0031.md).
- [fig-0034](../documents/src-000012/pdf-figures/fig-0034.md).

[Signature structure, rule details and limitations](../../../../concepts/bah-signature-guidelines.md) · [Signed-message business usage](signed-message.md)
